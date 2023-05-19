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

sys.setrecursionlimit(10**6) # 재귀 깊이 늘려주기
roof = 1000 # 반복 횟수 1000

#======================SelectionSort==========================
start = time.time() # time.time() ==> 스톱워치 시작
for _ in range(roof): # 1000번 반복
    A = [random.randint(0, 100) for _ in range(300)] # 0~100까지 난수 총 300개를 A 리스트에 저장
    selectionSort(A) # 함수 호출
end = time.time() # 스톱워치 종료
selectionS = (end-start)/roof # selectionSort의 런타임 평균값 저장
print('Selection sort avg (recusive) Processing Time : ', selectionS) # 평균값 출력

#=======================BubbleSort============================
start = time.time() # time.time() ==> 스톱워치 시작
for _ in range(roof): # 1000번 반복
    A = [random.randint(0, 100) for _ in range(300)] # 0~100까지 난수 총 300개를 A 리스트에 저장
    bubbleSort(A) # 함수 호출
end = time.time() # 스톱워치 종료
bubbleS = (end-start)/roof # bubbleSort의 런타임 평균값 저장
print('Bubble sort avg (recusive) Processing Time : ', bubbleS) # 평균값 출력

#=======================InsertSort============================
start = time.time() # time.time() ==> 스톱워치 시작
for i in range(roof): # 1000번 반복
    A = [random.randint(0, 100) for _ in range(300)] # 0~100까지 난수 총 300개를 A 리스트에 저장
    insertSort(A, len(A)) # 함수 호출
end = time.time() # 스톱워치 종료
insertS = (end-start)/roof # insertSort의 런타임 평균값 저장
print('Insert sort avg (recusive) Processing Time : ', insertS) # 평균값 출력

#=======================MergeSort=============================
start = time.time() # time.time() ==> 스톱워치 시작
for _ in range(roof): # 1000번 반복
    A = [random.randint(0, 100) for _ in range(300)] # 0~100까지 난수 총 300개를 A 리스트에 저장
    mergeSort(A) # 함수 호출
end = time.time() # 스톱워치 종료
mergeS = (end-start)/roof # mergeSort의 런타임 평균값 저장
print('Merge sort avg (recusive) Processing Time : ', mergeS) # 평균값 출력

#======================QuickSort============================
start = time.time() # time.time() ==> 스톱워치 시작
for _ in range(roof): # 1000번 반복
    A = [random.randint(0, 100) for _ in range(300)] # 0~100까지 난수 총 300개를 A 리스트에 저장
    quickSort(A) # 함수 호출
end = time.time() # 스톱워치 종료
quickS = (end-start)/roof # quickSort의 런타임 평균값 저장
print('Quick sort avg Processing Time : ', quickS) # 평균값 출력

#======================HeapSort=============================
start = time.time() # time.time() ==> 스톱워치 시작
for _ in range(roof): # 1000번 반복
    A = [random.randint(0, 100) for _ in range(300)] # 0~100까지 난수 총 300개를 A 리스트에 저장
    heapSort(A) # 함수 호출
end = time.time() # 스톱워치 종료
heapS = (end-start)/roof # heapSort의 런타임 평균값 저장
print('Heap sort avg Processing Time : ', heapS) # 평균값 출력

#======================ShellSort============================
start = time.time() # time.time() ==> 스톱워치 시작
for _ in range(roof): # 1000번 반복
    A = [random.randint(0, 100) for _ in range(300)] # 0~100까지 난수 총 300개를 A 리스트에 저장
    shellSort(A) # 함수 호출
end = time.time() # 스톱워치 종료
shellS = (end-start)/roof # shellSort의 런타임 평균값 저장
print('Shell sort avg Processing Time : ', shellS) # 평균값 출력

#======================그래프그리기===========================
plt.title('Arrangements Time Comparison') # 그래프 제목 설정
plt.xlabel('name of each sort') # x축 제목
plt.ylabel('time(sec)') # y축 제목
x = ['Selection','Bubble','Insert','Merge','Quick','Heap','Shell'] # x축 값
y = [selectionS, bubbleS, insertS, mergeS, quickS, heapS, shellS] # y축 값
plt.bar(x,y, color=['blue'],width=0.4) # 그래프 병합 (x,y), 막대 색 blue, 막대 넓이 0.4
plt.show() # 시각화