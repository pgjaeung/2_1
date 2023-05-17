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
import matplotlib.pyplot as plt

sys.setrecursionlimit(10**6)
roof = 1000

#======================SelectionSort==========================
start = time.time()
for _ in range(roof):
    A = [random.randint(0, 100) for _ in range(300)]
    selectionSort(A)
end = time.time()
selectionS = (end-start)/roof
print('Selection sort avg (recusive) Processing Time : ', selectionS)

#=======================BubbleSort============================
start = time.time()
for _ in range(roof):
    A = [random.randint(0, 100) for _ in range(300)]
    bubbleSort(A)
end = time.time()
bubbleS = (end-start)/roof
print('Bubble sort avg (recusive) Processing Time : ', bubbleS)

#=======================InsertSort============================
start = time.time()
for i in range(roof):
    A = [random.randint(0, 100) for _ in range(300)]
    insertSort(A, len(A))
end = time.time()
insertS = (end-start)/roof
print('Insert sort avg (recusive) Processing Time : ', insertS)

#=======================MergeSort=============================
start = time.time()
for _ in range(roof):
    A = [random.randint(0, 100) for _ in range(300)]
    mergeSort(A)
end = time.time()
mergeS = (end-start)/roof
print('Merge sort avg (recusive) Processing Time : ', mergeS)

#======================QuickSort============================
start = time.time()
for _ in range(roof):
    A = [random.randint(0, 100) for _ in range(300)]
    quickSort(A)
end = time.time()
quickS = (end-start)/roof
print('Quick sort avg Processing Time : ', quickS)

#======================HeapSort=============================
start = time.time()
for _ in range(roof):
    A = [random.randint(0, 100) for _ in range(300)]
    heapSort(A)
end = time.time()
heapS = (end-start)/roof
print('Heap sort avg Processing Time : ', heapS)

#======================ShellSort============================
start = time.time()
for _ in range(roof):
    A = [random.randint(0, 100) for _ in range(300)]
    shellSort(A)
end = time.time()
shellS = (end-start)/roof
print('Shell sort avg Processing Time : ', shellS)

#======================그래프그리기===========================
plt.title('Arrangements Time Comparison')
plt.xlabel('name of each sort')
plt.ylabel('time(sec)')
x = ['Selection','Bubble','Insert','Merge','Quick','Heap','Shell']
y = [selectionS, bubbleS, insertS, mergeS, quickS, heapS, shellS]
plt.bar(x,y, color=['blue'],width=0.4)
plt.show()