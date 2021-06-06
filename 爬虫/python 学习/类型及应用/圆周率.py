from random import random
from math  import sqrt
from time import perf_counter
DARTS  = 1200000
hits = 0
perf_counter()
for i in range(1,DARTS):
    x,y = random(),random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits+1
pi = 4* (hits/DARTS)
print('pi的值是%s'%pi)
print('程序运行时间是%-5.5ss'%perf_counter())