
import math
import random
import time
from datetime import datetime

animals = ['Duck', 'Jackel', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Bird', 'Pengwin', 'FIsh', 'Croc']


def count_animals():
    num_animals = 0
    for animal in animals:
        num_animals += 1
    return num_animals


print(count_animals())

# O(n)

# searching in an O(n)

'''
Assume arr is sorted, return True if target is in the array
'''

def binary_search(arr, target):
    # Set boundaries for low and high marks to search
    lo = 0
    hi = len(arr)
    # While low and high do not overlap...
    while lo < hi:
        # Check the midpoint
        mid = (lo + hi) // 2
        # If it's equal, return True
        if arr[mid] == target:
            return True
        # Else, if target is smaller
        elif target < arr[mid]:
            # set the high to midpoint value
            hi = mid - 1
        # Else if target is bigger
        else:
            # set the low to midpoint value
            lo = mid + 1
    # If we get to the end, return False
    return False


def insertion_sort(arr):
    # Divide your hand into sorted on the left and unsorted on the right
    # Sorted is just the first element
    # then go card by card and move them into place.
    # Loop through all elements in unsorted...
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i  # j is our sliding index
        # Shift sorted to the right until correct position found
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]  # Slide over one element
            j -= 1
        # Insert at that position
        arr[j] = temp
    return arr