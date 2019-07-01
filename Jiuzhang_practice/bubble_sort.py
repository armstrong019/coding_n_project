def swap(input_list, i, j):
    input_list = list(input_list)
    if (input_list[i] > input_list[j]):
        input_list[i], input_list[j] = input_list[j], input_list[i]
    print(input_list)
    return input_list


def inplace_bubble_sort(input_list):
    swapped = False
    while not swapped:
        swapped = True
        for i in range(len(input_list)-1):
            if (input_list[i] > input_list[i+1]):
                swapped = False
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                #swap(input_list, i, i + 1)

    return input_list


def bubble_sort(x):
    p1 = 0
    p2 = 1
    sorted = False
    while not sorted:
        flag = False
        while p2<=len(x)-1:
            if x[p1]>x[p2]:
                flag=True
                x[p1],x[p2] = x[p2],x[p1]
            p1+=1
            p2+=1
        if flag == True:
            sorted = False
            p1=0
            p2=1
        else:
            sorted = True

def bubble_sort2(x):
    sorted = False
    while not sorted:
        for i in range(len(x)-1):
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
                sorted= True
        if not sorted:
            break
        else:
            sorted=False

def bubble_sort3(x):
    for i in range(len(x)):
        for j in range(0, len(x)-1):
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
    return x

x = [-1, 2, 5, 3, 4, 1, 2]
#inplace_bubble_sort(x)
bubble_sort3(x)
# Should print [1, 2, 3, 4, 5]
print(x)


