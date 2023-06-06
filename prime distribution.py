from math import sqrt
from time import time

start = time()


def dgtlRoot(number):
    number = sum([int(char) for char in str(number)])
    if number >= 10:
        return dgtlRoot(number)
    return number

def primeRange(maxNum):
    start = time()
    primesNum = 0

    for num in range(10**(maxNum-1), 10**maxNum): # From one power to the next
        factors = [] # Stores factors, resets with each new number
        x = 1 # Incremented
        if (str(num)[-1] in '245680' and num not in [2,5]) \
                or (dgtlRoot(num) % 3 == 0 and num != 3):
            continue

        while x <= sqrt(num): # Square root not reached
            if num % 2 == 1 and x % 2 == 0: # if num odd and x is even
                pass # ...don't bother

            elif num % x == 0: # If a factor

                if x not in factors: # If factor not already stored
                    factors.append(x) # Store
                if int(num/x) not in factors: # If corresponding factor not stored
                    factors.append(int(num/x)) # then store
            if len(factors) > 2: # Can no longer be prime
                break # Break. Saves time.
            x += 1
        if len(factors) == 2:
            primesNum += 1

    end = time()

    # OUTPUT
    print(f'There are {primesNum} {maxNum}-digit prime numbers.\nThis is equal to \
{round(100*primesNum/((10**maxNum)-10**(maxNum-1)),2)}% of \
numbers in this range')
    print('Time taken: {} secs\n'.format(round(end-start,5)))

if __name__ == "__main__":
    for maxNum in range(1,10):
        primeRange(maxNum)
