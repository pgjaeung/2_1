def insertSort(arr, n):
    # 재귀 함수의 종료 조건: 배열의 길이가 1 이하인 경우
    if n <= 1:
        return

    # 마지막 요소를 제외한 부분 배열을 재귀적으로 정렬
    insertSort(arr, n-1)

    # 마지막 요소를 정렬된 부분 배열에 삽입
    last = arr[n-1]
    j = n-2

    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]  # 요소들을 오른쪽으로 이동
        j -= 1

    arr[j+1] = last  # 올바른 위치에 삽입
