from operator import mul
from functools import reduce

def multiply(number, steps = 0):
    if number < 10:
        print(number, f'Step {steps}')
        return number, steps
    else:
        print(number, f'Step {steps}')
        steps += 1
        number = reduce(mul, [int(digit) for digit in str(number)], 1)
        return multiply(number, steps)

while True:
    number = int(input("Enter number to check multiplicative persistence: "))
    multiply(number)