import pandas as pd
import numpy as np
import math
import operator
from sklearn import datasets
from sklearn.model_selection import train_test_split

data = datasets.load_iris()
#data = pd.read_csv('iris.csv')
x = np.array(data.data[:,:3])
y = np.array(data.target)

def euclidean_dist(data1, data2):
    return np.sqrt(np.sum((data1-data2)**2))


def knn(x_train, y_train, test_instance, k):
    dist = {}
    neigh =[]
    class_vote = {}
    # calculate the euclean distance between each row of the training data and test data
    for i in range(len(x_train)):
        dist[i] = euclidean_dist(x_train[i], test_instance)
    # sort the result according to distance
    sorted_dist = sorted(dist.items(), key=lambda kv:kv[1])
    # extracting top k neighbors
    for i in range(k):
        neigh.append(sorted_dist[i][0])
    print(neigh, sorted_dist)

    # vote for the class
    for j in range(k):
        iris_class = y_train[neigh[j]]
        if iris_class in class_vote:
            class_vote[iris_class]+=1
        else:
            class_vote[iris_class]=1
    # sort the vote
    sorted_vote = sorted(class_vote.items(), key=lambda kv:kv[1])
    print(class_vote)
    return sorted_vote[0][0]
#
#
#
#
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
# res = knn(x_train, y_train, x_test[0], 3)
# print('the class vote is {}'.format(res))


# compare this with sklearn result
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(x_train, y_train)
print(neigh.predict([x_test[0]]))