import sys
from time import time
import numpy as np
import matplotlib.pyplot as plt

sys.setrecursionlimit(100000)
mem = {}
def fib(num):
    if num < 0:
        raise ValueError("Negative arguments not allowed")
    if num in [0,1]:
        return num

    else:
        if num in mem:
            return mem[num]
    if num not in mem:
        mem[num] = fib(num-1) + fib(num-2)
        return mem[num]

'''Fibonacci recursive function with memoisation
for easy (speedy) recall when getting to higher numbers'''
# start = time()
# for x in range(900,1001):
#     try:
#         print(fib(x))
#     except:
#         print('Can\'t really do that one, mate.')
#         break
        # raise RecursionError("Poor")

end = time()
# print(end-start, 'secs')

plt.plot([x for x in range(51)], [fib(x) for x in range(51)])
plt.show()
