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


x = [5, 3, 4, 1, 2]
inplace_bubble_sort(x)
# Should print [1, 2, 3, 4, 5]
print(x)

