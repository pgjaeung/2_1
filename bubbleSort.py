def bubbleSort(arr): # bubbleSort라는 함수와 arr이라는 매개변수를 정의한다.
    if len(arr) <= 1: # 배열의 길이가 1이하인 경우
        return arr # arr을 리턴 (재귀함수 종료 조건)

    for i in range(len(arr) - 1): # arr의 첫 번째 원소 ~ arr의 끝 이전의 원소까지 반복
        if arr[i] > arr[i + 1]: # arr[i]번째가 그 다음번째보다 크면
            arr[i], arr[i + 1] = arr[i + 1], arr[i] # arr[i]번째에 i+1값을 넣고, arr[i+1]번째에 i값을 넣음. (교환, 더큰값이 뒤로 이동)

    return bubbleSort(arr[:-1]) + [arr[-1]] # 맨 뒤의 요소를 제외한 나머지 부분 배열에 대해 재귀 호출