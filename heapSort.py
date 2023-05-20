def heapSort(arr): # heapSort를 정의한다. 매개변수로 arr을 받는다.
    n = len(arr) # n에 arr의 길이를 넣는다.
    for i in range(n // 2 - 1, -1, -1): # n에 /2 -1 연산을 취한 값부터 0까지 역순으로 1씩 감소
        heapify(arr, n, i) # heapify함수의 매개변수로 넣고 함수호출한다.
    for i in range(n - 1, 0, -1): # n - 1부터 i--해서 i가 0보다 클때까지 반복
        arr[0], arr[i] = arr[i], arr[0] # 최대값을 배열의 끝으로 이동
        heapify(arr, i, 0) # 힙 조정
    return arr # 배열반환

def heapify(arr, n, i): # heapify함수 정의, 매개변수로 arr, n ,i
    largest = i  # 부모 노드
    left = 2 * i + 1  # 왼쪽 자식 노드
    right = 2 * i + 2  # 오른쪽 자식 노드

    if left < n and arr[left] > arr[largest]: # 왼쪽 자식노드가 부모노드보다 크면
        largest = left # largest에 왼쪽 노드값 넣음
    if right < n and arr[right] > arr[largest]: # 오른쪽 자식노드가 largest보다 크면
        largest = right # largest에 오른쪽 노드값 넣음
    if largest != i: #largest가 i가 아닌경우(위의 조건문으로 인해 값이 바뀐경우)
        arr[i], arr[largest] = arr[largest], arr[i] # 해당 노드와 자식노드 교환
        heapify(arr, n, largest) # 재귀호출