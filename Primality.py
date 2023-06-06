from math import sqrt, log2
from random import randint, choice

def dgtlRoot(number):
    number = sum([int(char) for char in str(number)])
    if len(str(number)) != 1:
        return dgtlRoot(number)
    return number

def prime(num): # Slightly different to prime finder.py
    # Presents reasons for (non-)primality
        factors = []
        x = 1
        if (str(num)[-1] in '245680'\
                and num not in [2,5]):
            print('Final digit!')
            pass
        elif (dgtlRoot(num) % 3 == 0\
              and num != 3):
            print('Digital root shows...')
            return False
        while x <= sqrt(num):
            if (num % 2 == 1\
                    and x % 2 == 0):
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
            print('Two factors.')
            return True
        else:
            proper = [y for y in factors if y not in [1, num]]
            print(f'More than two factors. {proper}')
            return False

while True:
    entryVal = False
    while not entryVal:
        try:
            entry = int(input('Enter number to check primality: '))
            entryVal = True
        except ValueError:
            print('Please enter a valid number.\n')
    # entry = ''
    # for x in range(10**2):
    #     if x is 0:
    #         entry += str(randint(1,9))
    #     elif x is 10**2-1:
    #         entry += str(choice([1,3,7,9]))
    #     else:
    #         entry += str(randint(0,9))
    # print(f'Testing {len(entry)}-digit number.')
    # entry = int(entry)
    if prime(entry):
        print(f'Is prime.\n')
    else:
        print(f'Is NOT prime.\n')