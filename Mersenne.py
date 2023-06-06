#!/usr/bin/env pypy
from math import sqrt

def sumDigits(number):
    number = sum([int(char) for char in str(number)])
    if len(str(number)) != 1: return sumDigits(number)
    return number

def prime(num):
        factors = []
        x = 1
        if (str(num)[-1] in '245680' and num not in [2,5])\
                or (sumDigits(num) % 3 == 0 and num != 3):
            return False
        while x <= sqrt(num):
            if num % 2 == 1 and x % 2 == 0:
                pass
            elif num % x == 0:
                if x not in factors:
                    factors.append(x)
                if int(num/x) not in factors:
                    factors.append(int(num/x))
            if len(factors) > 2:
                break
            x += 1
        if len(factors) == 2:
            return True
        else:
            return False

def mersenne():
    exp = 0
    mersCount = 0
    while 1 == 1:
        if prime(exp):
            print('Trying exponent:', exp)
            if prime(2**exp - 1):
                mersCount += 1
                print(f'M{mersCount}:',2**exp - 1, f'- Power {exp}')
        exp += 1

if __name__ == '__main__':
    mersenne()