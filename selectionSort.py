def selectionSort(arr):
    if len(arr) <= 1:
        return arr

    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i

    arr[0], arr[min_idx] = arr[min_idx], arr[0]

    return [arr[0]] + selectionSort(arr[1:])
