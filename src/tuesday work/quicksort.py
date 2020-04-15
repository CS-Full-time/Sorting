

def quicksort(arr):
    # base case: arr len 0 or 1 is sorted
    print(arr)
    if len(arr) <= 1:
        return arr
    # pick pivot
    pivot = arr[0]
    # separate all vals smaller and larger than pivot
    smaller = []
    larger = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    # sort smaller and larger
    smaller = quicksort(smaller)
    larger = quicksort(larger)
    # concatenate smaller + pivot + larger
    return smaller + [pivot] + larger



    