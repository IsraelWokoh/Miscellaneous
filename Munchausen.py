def munc(num):
    return sum(int(ch)**int(ch) for ch in str(num)) == num

for x in range(1, 10**10):
    if munc(x): print(x)