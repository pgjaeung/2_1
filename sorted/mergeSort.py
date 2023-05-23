def mergeSort(arr): # mergeSort를 정의한다. 매개변수로 arr을 받는다
    if len(arr) <= 1: # 배열의 길이가 1이하인 경우
        return arr # arr을 리턴 (재귀함수 종료 조건)

    mid = len(arr) // 2 # mid 변수에 배열의 절반의 길이를 넣는다.
    left = arr[:mid] # left 변수에 배열의 시작 ~ mid(절반의 길이) 까지 넣는다.
    right = arr[mid:] # right 변수에 mid(절반의 길이) ~ 배열의 끝까지 넣는다.

    left = mergeSort(left) # mid기준 왼쪽 리스트를 재귀적으로 정렬
    right = mergeSort(right) # mid기준 오른쪽 리스트를 재귀적으로 정렬

    return merge(left, right) # 아래 merge함수의 매개변수값으로 left와 right를 리턴


def merge(left, right): # merge를 정의한다. 매개변수로 left와 right를 받는다.
    merged = [] # merged라는 새로운 리스트를 생성한다. (병합목적 리스트)
    i, j = 0, 0 # i와 j를 각각 0으로 초기화한다.

    # 두 부분 배열을 비교하며 병합
    while i < len(left) and j < len(right): # i와 j가 각각 left리스트의 길이와 right리스트의 길이보다 작을때까지 반복
        if left[i] <= right[j]: # left가 right보다 작거나 같을 때
            merged.append(left[i]) # 작은값 (left)를 merged 리스트에 넣는다.
            i += 1 # 증감자
        else: # right가 left보다 작거나 같을 때
            merged.append(right[j]) # 작은 값 (right)를 merged 리스트에 넣는다.
            j += 1 # 증감자
    while i < len(left): # 위 반복문과 같다. 목적은 남은 요소들의 병합이다.
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged # 최종적으로 정렬된 리스트를 리턴한다.