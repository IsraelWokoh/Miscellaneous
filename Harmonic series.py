from time import time

total = 0
denom = 1
run = True
target = 1

while run:
    start = time()
    while total < target:
        total += 1/denom
        denom += 1
    end = time()
    print(total,  denom, f'{end-start} secs', \
        f'- {round(denom/(1000000*(end-start)), 3)}M op/sec')
    target += 1