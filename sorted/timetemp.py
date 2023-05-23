import time
import random
import sys
from insertSort import *

roof = 100

start = time.time()
for i in range(roof):
    A = [random.randint(0, 100) for _ in range(300)]
    insertSort(A, len(A))
end = time.time()
print('Insert sort (recusive) Processing Time : ', (end-start))
