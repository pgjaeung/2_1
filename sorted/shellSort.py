def shellSort(arr): # quickSort를 정의한다. 매개변수로 arr을 받는다
    n = len(arr) # n에 arr의 길이를 담는다
    gap = n // 2 # gap에 n의 반 값을 담는다
    # gap을 점차 줄여가며 삽입 정렬 수행
    while gap > 0: # gap이 0보다 클 때
        for i in range(gap, n): # i가 gap ~ n까지
            temp = arr[i] # 임시변수 temp에 arr[i]값을 담는다
            j = i # j에 i값을 넣는다.
            while j >= gap and arr[j - gap] > temp: # j가 gap보다 크거나 같고, arr[j-gap]이 temp보다 클 때
                arr[j] = arr[j - gap] # arr[j]에 arr[j - gap]값을 넣는다. (삽입정렬 수행)
                j -= gap # 증감자
            arr[j] = temp # arr[j]에 temp 값을 넣는다.
        gap //= 2 # gap = gap//2
    return arr # arr반환