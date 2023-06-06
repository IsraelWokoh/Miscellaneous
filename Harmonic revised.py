"""
Using Nicolo Oresme's proof of divergence, we know an upper bound for
required number of 1/x fractions, when summed, to exceed any integer n.
"""

from math import log2

total = 0
denom = 1
run = True
target = 1

while run:
    halves = 2 * (target - 1)
    maxDenom = 2**halves

    while denom <= maxDenom:
        total += 1/denom
        denom += 1
    print(total, target, f'2^{int(log2(maxDenom))}', f'Overshoot: {total - target}, {round(100 * (total / target - 1), 2)}%')
    target += 1