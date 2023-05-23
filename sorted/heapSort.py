def heapSort(arr):
    n = len(arr)

    # 최대 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 힙에서 요소 하나씩 꺼내서 정렬
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 최대값을 배열의 끝으로 이동
        heapify(arr, i, 0)  # 힙 조정

    return arr


def heapify(arr, n, i):
    largest = i  # 부모 노드
    left = 2 * i + 1  # 왼쪽 자식 노드
    right = 2 * i + 2  # 오른쪽 자식 노드

    # 왼쪽 자식 노드가 부모 노드보다 크면 largest 갱신
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식 노드가 largest보다 크면 largest 갱신
    if right < n and arr[right] > arr[largest]:
        largest = right

    # largest가 변경되었을 경우 해당 노드와 자식 노드 교환
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
