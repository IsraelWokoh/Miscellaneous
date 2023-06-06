from math import sqrt, log2
from random import randint, choice

def dgtlRoot(number):
    number = sum([int(char) for char in str(number)])
    if len(str(number)) != 1:
        return dgtlRoot(number)
    return number

def prime(num): # Slightly different to prime finder.py
    # Presents reasons for (non-)primality
    if num == 1:
        return False
    else:
        factors = set()
        x = 1
        if (str(num)[-1] in '245680'\
                and num not in [2,5]):
            # print('Final digit!')
            pass
        elif (dgtlRoot(num) % 3 == 0\
              and num != 3):
            # print('Digital root shows...')
            return False
        while x <= sqrt(num):
            if (num % 2 == 1 and not x % 2):
                pass
            elif not num % x:
                factors.update((x, num//x))
                if len(factors) > 2:
                    return False
            x += 1
        if len(factors) == 2:
            # print('Two factors.')
            return True

entry = 1
while True:
    # entryVal = False
    # while not entryVal:
    #     try:
    #         entry = int(input('Enter number to check primality: '))
    #         entryVal = True
    #     except ValueError:
    #         print('Please enter a valid number.\n')
    poly = entry**2+entry+41
    print(f'n = {entry}')
    if prime(poly):
        print(f'{poly} is prime.\n')
    else:
        print(f'{poly} is NOT prime.\n')
        break
    entry += 1