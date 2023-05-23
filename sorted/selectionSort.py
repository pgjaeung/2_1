def selectionSort(arr): # selectionSort를 정의한다. 매개변수로 arr을 받는다
    if len(arr) <= 1: # 매개변수 arr의 길이가 1의 이하라면
        return arr # arr을 리턴하고 종료

    min = 0 # min_idx라는 가장 작은 값을 0으로 초기화한다.
    for i in range(1, len(arr)): # 1번 인덱스부터 arr의 길이까지
        if arr[i] < arr[min]: # arr의 i번째 요소가 arr의 (초기값 0)의 요소보다 작으면
            min = i # min_idx에 그 값을 넣는다. (더 작은값)

    arr[0], arr[min] = arr[min], arr[0] # 선택정렬에서 자주 사용되는 교환방식으로, arr[0]번째 원소와 min번째 원소를 교환

    return [arr[0]] + selectionSort(arr[1:]) # 재귀호출을 통해 정렬한 리스트를 다시 결합하여 최종적으로 정렬된 리스트를 얻을 수 있다.
