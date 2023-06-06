from time import time
from sys import maxsize
from math import log as ln, log10, log1p, log2
from math import e
# start = time()
# for x in range(51):
#     ans = ((x**x)+1)/(x+1)
#     if ans % 1 == 0: print(f'{x} gives {int(ans)}')
# end = time()
# print(f'Took {end-start} seconds.')
# print(time())

memo = {}
def fact(x):
    if x in [0,1]:
        return 1
    elif x not in memo:
        memo[x] = x*fact(x-1)
    return memo[x]



n=1
while 1 is 1:
    total = 0
    for x in range(n):
        total += 1/fact(x)
    if n % 10**3 is 0:
        print(f'{n} - {total}')
    n+=1
'''NOTE
Calculating Euler's number using (1+1/n)^n is hugely inaccurate.
Summation of factorial reciprocals are much better (though I can't get past
~16 digits of precision

Past 500, fact() w/o memo is very slow. With it... gah damn.'''
# total = 0
# bench = time()
# for x in range(1001):
#     # if x % 1000000 == 0:
#     print((1 + (1 / (10 ** x))) ** (10 ** x))
# print(total)
# # sum([(1+1/x)**x for x in range(1,maxsize)])
# x=0
# # print(log2(8), log10(10), ln(e), log1p(1.61803398875))
# print(maxsize**100)
# # while x**x < fact(x)

for x in range(100):
    print((-1)**(x%2))
# 1/2*1-1 + 1/2*2-1
max = 1
while 1 is 1:
    total = 0
    for x in range(1, max+1):
        print((-1)**(max))
    print(4*total)
    max += 1

print('Done')