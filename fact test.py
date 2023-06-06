from math import log10, floor
def fact(num):
    if num in [0, 1]:
        return 1
    else:
        return num * fact(num - 1)
x = 1
while True:
    try:
        print(str(floor(log10((x**x)-(fact(x))))+1) + ' digits')
    except ValueError:
        print('No value')
    x+=1