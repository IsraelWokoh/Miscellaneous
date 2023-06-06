from time import time

def fact(x):
    if x in [0,1]:
        return 1
    else:
        if x in mem:
            return mem[x]
        else:
            mem[x] = x*fact(x-1)
            if x-1 in mem:
                mem.pop(x-1)
            return mem[x]

mem = {}
x, num = 1, 1
while 1 is 1:
    start = time()
    while fact(x) <= x**(num*1000):
        x += 1
    end = time()
    num += 1
    print(f'{x}! > {num*1000}th power - {round(end-start,6)} secs')