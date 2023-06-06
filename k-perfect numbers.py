from math import log10

def getFactors(num):
    factors = set()
    for x in range(1, int(num**0.5)+1):
        if not num%x:
            for factor in {x,num//x}:
                factors.add(factor)
    return factors

print('----- k-PERFECT NUMBER: σ(n) = kn, k ∈ ℕ -----')
for num in range(1, 10**9):
    factorSum = sum(getFactors(num))
    if not factorSum % num:
        # print(f'{sigmaNum}/{num} = {sigmaNum/num}')
        print(f'{num} is a {factorSum // num}-perfect number.')
    if not log10(num) % 1:
        print(f'\n>>REACHED 10^{int(log10(num))}<<\n')