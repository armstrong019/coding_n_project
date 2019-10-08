import os
import sys
import tables
import pickle
import hashlib
from ast import literal_eval
import numpy as np
import matplotlib.pyplot as plt

from argparse import ArgumentParser
import logging
import warnings

import tensorflow as tf
import keras
from keras import backend as K
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras.layers import BatchNormalization
from keras.layers import Concatenate
from keras.layers import Convolution1D
from keras.layers import MaxPooling1D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Input
from keras.models import Sequential
from keras.models import Model
from keras.models import load_model
from livelossplot import PlotLossesKeras

from DataGenerator import DataGenerator
from helper import get_train_test_IDs


def binary_classification_deep_causal_cnn_model(num_input_timesteps, num_input_features, num_layers, kernel_size,
                                                filters_per_layer):
    model = Sequential(name="causal_cnn{}".format(num_layers))
    for k in range(num_layers):
        if k == 0:
            model.add(Convolution1D(filters=filters_per_layer[k],
                                    kernel_size=kernel_size,
                                    activation='relu',
                                    padding='causal',
                                    use_bias=True,
                                    input_shape=(num_input_timesteps, num_input_features)))
        else:
            model.add(Convolution1D(filters=filters_per_layer[k],
                                    kernel_size=kernel_size,
                                    activation='relu',
                                    padding='causal',
                                    use_bias=True))
            #             model.add(MaxPooling1D())

    model.add(Flatten())
    model.add(Dense(2, activation='softmax'))
    return model


def dilatedCNN_model(num_input_timesteps, num_input_features, wavenet_num_layers, wavenet_kernel_size,
                     wavenet_filters_per_layer):
    input_layer = Input(shape=(num_input_timesteps, num_input_features))
    output_layers = []
    for rep in range(wavenet_num_layers):
        A = input_layer
        for i in range(int(np.log2(num_input_timesteps))):
            A = Convolution1D(filters=wavenet_filters_per_layer[rep], kernel_size=wavenet_kernel_size, padding='causal',
                              dilation_rate=2 ** i, activation='relu')(A)
        output_layers.append(A)

    net = Concatenate(axis=-1)(output_layers)
    net = Flatten()(net)
    net = Dense(2, activation='softmax')(net)
    model = Model(input_layer, net)
    model.name = 'dilatedCNN'
    return model


def wavenetBlock(n_filters, kernel_size, dilation_rate):
    def f(input_):
        residual = input_

        tanh_out = Convolution1D(filters=n_filters, kernel_size=kernel_size, padding='causal',
                                 dilation_rate=dilation_rate, activation='tanh')(input_)

        sigmoid_out = Convolution1D(filters=n_filters, kernel_size=kernel_size, padding='causal',
                                    dilation_rate=dilation_rate, activation='sigmoid')(input_)

        merged = Multiply()([tanh_out, sigmoid_out])
        skip_out = Convolution1D(filters=1, kernel_size=1, padding='same')(merged)
        out = Add()([skip_out, residual])
        return out, skip_out

    return f


def wavenet_model(num_input_timesteps, num_input_features, wavenet_num_layers, wavenet_kernel_size,
                  wavenet_filters_per_layer):
    input_layer = Input(shape=(num_input_timesteps, num_input_features))
    A = input_layer
    skip_connections = []
    for rep in range(wavenet_num_layers):
        for i in range(int(np.log2(num_input_timesteps / 2))):
            A, B = wavenetBlock(n_filters=wavenet_filters_per_layer[rep], kernel_size=wavenet_kernel_size,
                                dilation_rate=2 ** i)(A)
            skip_connections.append(B)
    net = Add()(skip_connections)
    net = Activation('relu')(net)
    net = Convolution1D(filters=1, kernel_size=1, activation='relu')(net)
    net = Convolution1D(filters=1, kernel_size=1)(net)
    net = Flatten()(net)
    net = Dense(2, activation='softmax')(net)
    model = Model(input_layer, net)
    model.name = 'wavenet'
    return model


class LoggerCallback(keras.callbacks.Callback):
    def __init__(self, printer=print):
        keras.callbacks.Callback.__init__(self)
        self.printer = printer

    def on_train_begin(self, logs={}):
        self.printer('Start training')

    # TODO(avinash) : Include batch tracker
    # def on_batch_begin(self, batch, logs={}):
    #    msg = 'Batch {}/{}'.format(batch, logs.get('size', 0))
    #    self.printer(msg)

    def on_epoch_end(self, epoch, logs={}):
        msg = 'Epoch: {}, {}'.format(epoch + 1, ', '.join('{}: {}'.format(k, v) for k, v in logs.items()))
        self.printer(msg)


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--neighbors',
                        dest='neighbors',
                        type=int,
                        default=0,
                        help='include neighbors in input_data or not')

    parser.add_argument('--hist_len',
                        dest='hist_len',
                        type=int,
                        default=20,
                        help='hist_len')

    parser.add_argument('--pred_len',
                        dest='pred_len',
                        type=int,
                        default=20,
                        help='pred_len')

    parser.add_argument('--kernel_size',
                        dest='kernel_size',
                        type=int,
                        default=3,
                        help='kernel_size')

    parser.add_argument('--num_layers',
                        dest='num_layers',
                        type=int,
                        default=1,
                        help='num_layers')

    parser.add_argument('--filters_per_layer',
                        dest='filters_per_layer',
                        type=str,
                        default='[6]',
                        help='filters_per_layer')

    parser.add_argument('--model_name',
                        dest='model_name',
                        type=str,
                        default='deep_causal_cnn',
                        help='which model to use')

    parser.add_argument('--gpu_id',
                        dest='gpu_id',
                        type=str,
                        default='0',
                        help='which gpu')

    parser.add_argument('--gpu_memory_fraction',
                        dest='gpu_memory_fraction',
                        type=float,
                        default=0.3,
                        help='what fraction of gpu memory to use')

    namespace = parser.parse_args()
    neighbors = namespace.neighbors
    hist_len = namespace.hist_len
    pred_len = namespace.pred_len
    kernel_size = namespace.kernel_size
    num_layers = namespace.num_layers
    filters_per_layer = literal_eval(namespace.filters_per_layer)
    model_name = namespace.model_name
    gpu_id = namespace.gpu_id
    gpu_memory_fraction = namespace.gpu_memory_fraction

    path_name = '/home/Fang/data/tree_repr/'
    file_name = 'per_branch_training_data_tree_us_101_history_length_' + str(hist_len) + '_prediction_length_' + str(
        pred_len) + '.h5'

    pickle_train_filename = 'balanced_train_IDs_per_maneuver_binarylabel_history_length_' + \
                            str(hist_len) + '_prediction_length_' + str(pred_len) + '_ratio_1'
    pickle_test_filename = 'balanced_test_IDs_per_maneuver_binarylabel_history_length_' + \
                           str(hist_len) + '_prediction_length_' + str(pred_len) + '_ratio_1'
    train_IDs, test_IDs = get_train_test_IDs(path_name, pickle_train_filename, pickle_test_filename)
    train_IDs = train_IDs['Type00'] + train_IDs['Type01'] + train_IDs['Type10'] + train_IDs['Type11']
    test_IDs = test_IDs['Type00'] + test_IDs['Type01'] + test_IDs['Type10'] + test_IDs['Type11']

    # parameters
    num_examples = len(train_IDs)
    batch_size = 64

    if neighbors:
        input_feature_indecis = [0, 1, 5, 6, 10, 11, 15, 16, 20, 21, 25, 26, 30, 31]
    else:
        input_feature_indecis = [0, 1]

    output_feature_indecis = [0, 1]

    data_generator = DataGenerator(path_name,
                                   file_name,
                                   list_IDs=train_IDs,
                                   batch_size=batch_size,
                                   hist_len=hist_len,
                                   pred_len=pred_len,
                                   input_feature_indecis=input_feature_indecis,
                                   output_feature_indecis=output_feature_indecis,
                                   shuffle=True,
                                   return_output_data=False,
                                   return_label=True)
    data_generator.on_epoch_end()
    input_data, label = data_generator.__getitem__(0)
    input_data.shape

    num_input_timesteps = input_data.shape[1]
    num_input_features = input_data.shape[2]

    # setup logger
    FORMAT = '%(asctime)s %(process)d %(message)s'
    logging.basicConfig(format=FORMAT, stream=sys.stdout, level=logging.INFO)
    logger = logging.info

    model_dir = 'md_categorical_' + model_name + \
                '_neighbors' + str(neighbors) + \
                '_hist_len' + str(hist_len) + \
                '_pred_len' + str(pred_len) + \
                '_layers' + str(num_layers) + \
                '_kernel' + str(kernel_size) + \
                '_filters' + str(filters_per_layer) + '_test'

    logger('Building model')
    if model_name == 'deep_causal_cnn':
        model = binary_classification_deep_causal_cnn_model(num_input_timesteps,
                                                            num_input_features,
                                                            num_layers,
                                                            kernel_size,
                                                            filters_per_layer)
    elif model_name == 'dilatedCNN':
        model = dilatedCNN_model(num_input_timesteps,
                                 num_input_features,
                                 num_layers,
                                 kernel_size,
                                 filters_per_layer)

    initial_epoch = 0

    if not os.path.exists('/home/Fang/model_results/checkpoints/' + model_dir):
        os.makedirs('/home/Fang/model_results/checkpoints/' + model_dir)
    # Checkpoint save path
    filepath = '/home/Fang/model_results/checkpoints/' + model_dir + '/{epoch:02d}-{loss:.2f}.hdf5'
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True)
    cbacks = []
    cbacks.append(checkpoint)
    cbacks.append(TensorBoard(log_dir='/home/marzieh/model_results/logs/' + model_dir))

    # define the optimizer
    opt = keras.optimizers.Adam(lr=0.001, decay=1e-6)
    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy', 'categorical_crossentropy'])

    train_data_generator = DataGenerator(path_name,
                                         file_name,
                                         list_IDs=train_IDs,
                                         batch_size=batch_size,
                                         hist_len=hist_len,
                                         pred_len=pred_len,
                                         input_feature_indecis=input_feature_indecis,
                                         output_feature_indecis=output_feature_indecis,
                                         shuffle=True,
                                         return_output_data=False,
                                         return_label=True)
    train_data_generator.on_epoch_end()

    test_data_generator = DataGenerator(path_name,
                                        file_name,
                                        list_IDs=test_IDs,
                                        batch_size=batch_size,
                                        hist_len=hist_len,
                                        pred_len=pred_len,
                                        input_feature_indecis=input_feature_indecis,
                                        output_feature_indecis=output_feature_indecis,
                                        shuffle=True,
                                        return_output_data=False,
                                        return_label=True)
    test_data_generator.on_epoch_end()

    logger('Begin training')
    # Set `use_multiprocessing` to False and `workers` to 1 for now
    # TODO(avinash): Check if multiprocessing can be used

    # train model

    # train model
    os.environ["CUDA_VISIBLE_DEVICES"] = gpu_id
    device = "/gpu:0"
    with tf.device(device):
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        session = tf.Session(config=config)
        K.set_session(session)

        model.fit_generator(generator=train_data_generator,
                            steps_per_epoch=num_examples // (batch_size),
                            epochs=10000,
                            callbacks=cbacks,
                            validation_data=test_data_generator,
                            validation_steps=20,
                            initial_epoch=initial_epoch,
                            verbose=0
                            )
