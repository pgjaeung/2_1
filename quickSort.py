def quickSort(arr):
    # 재귀 함수의 종료 조건: 배열의 길이가 1 이하인 경우
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 피벗을 배열의 중간 요소로 선택
    left = []
    right = []
    equal = []

    # 피벗을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽, 같은 값은 equal에 저장
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)

    # 왼쪽과 오른쪽 부분 배열을 재귀적으로 정렬하고, 피벗과 같은 값을 결합하여 반환
    return quickSort(left) + equal + quickSort(right)


