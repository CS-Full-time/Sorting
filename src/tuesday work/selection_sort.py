def selection_sort( arr ):
    # loop through n-1 elements
    # (n-1 because after the sort, the one remaining will be the largest)
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # (hint, can do in 3 loc)
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr
​