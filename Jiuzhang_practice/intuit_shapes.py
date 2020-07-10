#https://stackoverflow.com/questions/1984162/purpose-of-pythons-repr
class Shape:
    def __init__(self, kind, payload=None):
        self.kind = kind
        self.payload = payload

    def __repr__(self):
        return self.kind.__repr__()

input_list = [
    Shape("triangle", "Some"),
    Shape("circle", "Random"),
    Shape("triangle", "Payload"),
    Shape("square", "Data"),
    Shape("circle", "Data"),
]
x = Shape("triangle", "Some")
print(repr(x))
print(repr(x) == "'triangle'")

def sort_shape(input_list):
    dic_count ={'circle':0, 'square':0, 'triangle':0}
    for shape in input_list:
        print('shape is', shape)
        if repr(shape) == "'triangle'":
            dic_count['triangle']+=1
        elif repr(shape) == "'circle'":
            dic_count['circle']+=1
        else:
            dic_count['square']+=1
    ic = 0
    isq = dic_count['circle']
    itr = dic_count['circle']+dic_count['square']
    output = [None for _ in range(len(input_list))]
    for shape in input_list:
        if repr(shape) == "'circle'":
           output[ic] = shape
           ic+=1
        elif repr(shape) == "'square'":
            output[isq] = shape
            isq+=1
        else:
            output[itr] = shape
            itr+=1
    for out in output:
        print(out)

sort_shape(input_list)


