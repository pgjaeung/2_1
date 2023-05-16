def mergeSort(arr):
    # 재귀 함수의 종료 조건: 배열의 길이가 1 이하인 경우
    if len(arr) <= 1:
        return arr

    # 배열을 반으로 나누기
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 각 부분 배열을 재귀적으로 정렬
    left = mergeSort(left)
    right = mergeSort(right)

    # 두 개의 정렬된 부분 배열을 병합
    return merge(left, right)


def merge(left, right):
    merged = []
    i, j = 0, 0

    # 두 부분 배열을 비교하며 병합
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # 남은 요소들을 병합
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged