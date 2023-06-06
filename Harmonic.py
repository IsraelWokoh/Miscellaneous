from time import time
from multiprocessing import process

total = 0
denom = 1
run = True
target = 1

while run:
    start = time()
    while total < target:
        total += 1/denom
        if total >= target:
            end = time()
            print(total,  denom, '{} secs'.format(end-start), '- {} op/sec'.format(denom/(end-start)))
        denom += 1
    target += 1