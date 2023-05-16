def bubbleSort(arr):
    # 재귀 함수의 종료 조건: 배열의 길이가 1 이하인 경우
    if len(arr) <= 1:
        return arr

    # 한 번의 패스를 통해 최대값을 맨 뒤로 이동시킴
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # 맨 뒤의 요소를 제외한 나머지 부분 배열에 대해 재귀 호출
    return bubbleSort(arr[:-1]) + [arr[-1]]