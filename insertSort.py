def insertSort(arr, n): # insertSort를 정의한다. 매개변수로 arr과 n을 받는다
    if n <= 1: # 배열의 길이가 1이하인 경우
        return # return == return None

    insertSort(arr, n-1) # 배열의 마지막 요소를 제외한 부분을 재귀 호출

    last = arr[n-1] # last변수에 arr의 마지막 요소를 정렬된 부분 배열에 삽입
    j = n-2 # j 변수에 n-2값 넣음

    while j >= 0 and arr[j] > last: # j가 0보다 크거나 같고 arr[j]가 last값보다 클 때
        arr[j+1] = arr[j]  # 요소들을 오른쪽으로 이동
        j -= 1 # 증감자

    arr[j+1] = last  # last 값을 arr[j+1](올바른 위치)에 삽입
