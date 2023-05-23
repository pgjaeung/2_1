def quickSort(arr): # quickSort를 정의한다. 매개변수로 arr을 받는다
    if len(arr) <= 1: # 배열의 길이가 1이하인 경우
        return arr # arr을 리턴 (재귀함수 종료 조건)

    pivot = arr[len(arr) // 2]  # pivot변수를 배열의 중간 요소로 선택
    left = [] # left 빈 리스트 생성
    right = [] # right 빈 리스트 생성
    equal = [] # equal 빈 리스트 생성

    for num in arr: # num이 arr에 있으면
        if num < pivot: # pivot보다 작은 값은
            left.append(num) # left 리스트에 추가
        elif num > pivot: # pivot보다 큰 값은
            right.append(num) # right 리스트에 추가
        else: # 둘 다 아닐경우(같을 경우)
            equal.append(num) # equal 리스트에 추가

    return quickSort(left) + equal + quickSort(right) # left와 right를 재귀적으로 정렬하고 pivot과 같은 값을 결합하여 리턴


