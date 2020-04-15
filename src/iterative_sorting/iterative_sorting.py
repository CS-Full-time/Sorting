# TO-DO: Complete the selection_sort() function below

import random
list = random.sample(range(1, 20), 10)

# list = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
              # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    changes = True
    while changes:
        changes = False
        for i in range(1, len(arr)):
            # print(arr)
            if arr[i - 1] > arr[i]:
                # print("yes")
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                # print(arr)
                changes = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr


NewList = list

print(f'Original list: {NewList}')

print(f'Selection Sort: {selection_sort(NewList)}')
print(f'Bubble Sort: {bubble_sort(NewList)}')