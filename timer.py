from selectionSort import *
from bubbleSort import *
from insertSort import *
from mergeSort import *
from quickSort import *
from heapSort import *
from shellSort import *
import random
import time
import sys

sys.setrecursionlimit(10**6)
roof = 1000

B=[]
for value in range(0, 300):
    B.append(random.randint(0,100))

A=B.copy()
start = time.time()
selectionSort(A)
end = time.time()
print('Selection sort (recusive) Processing Time : ', end-start)

A=B.copy()
start = time.time()
bubbleSort(A)
end = time.time()
print('Bubble sort (recusive) Processing Time : ', end-start)

A=B.copy()
start = time.time()
insertSort(A,len(A))
end = time.time()
print('Insert sort (recusive) Processing Time : ', end-start)

A=B.copy()
start = time.time()
mergeSort(A)
end = time.time()
print('Merge sort (recusive) Processing Time : ', end-start)

A=B.copy()
start = time.time()
quickSort(A)
end = time.time()
print('Quick sort Processing Time : ', end-start)

A=B.copy()
start = time.time()
heapSort(A)
end = time.time()
print('Heap sort Processing Time : ', end-start)

A=B.copy()
start = time.time()
shellSort(A)
end = time.time()
print('Shell sort Processing Time : ', end-start)