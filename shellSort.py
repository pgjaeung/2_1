def shellSort(arr):
    n = len(arr)
    gap = n // 2
    # gap을 점차 줄여가며 삽입 정렬 수행
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # 삽입 정렬 수행
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr