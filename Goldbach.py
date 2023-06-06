'''
select even number - 24
generate ODD primes up to even number - 3, 5, 7, 11...
    prime[0]: - 3
        + prime[1] - 5
        + prime[2] - 7
        (subsequent primes > prime[0])
        ...
        until prime sum > even number or primes exhausted
    prime[1]: - 5
        + prime[2] - 7
        + prime[3] - 11
        ...
    ...
    until prime[x] > even number

    for each pair forming the even number, add to list

select next even number - 26
generate more ODD primes - avoid regeneration!
...
'''

from math import sqrt

def dgtlRoot(number):
    number = sum([int(char) for char in str(number)])
    if number >= 10: return dgtlRoot(number)
    return number

def genOddPrimes(evenNum):
    for num in range(evenNum - 999, evenNum + 1): # From the last even number to the next...
        factors = [] # Stores factors, resets with each new number
        x = 1 # Incremented

        # Digital Root/Final digit NON-PRIME criteria
        if (str(num)[-1] in '245680' and num not in [5]) or \
                (dgtlRoot(num) % 3 == 0 and num != 3): # [5] should be [2,5], but...
            #...we're excluding odd primes
            continue # Skips

        while x <= sqrt(num): # Square root not reached
            if num % 2 == 1 and x % 2 == 0: # if num odd and x is even
                pass # ...don't bother

            elif num % x == 0: # If a factor

                if x not in factors: # If factor not already stored
                    factors.append(x) # Store
                if int(num/x) not in factors: # If corresponding factor not stored
                    factors.append(int(num/x)) # then store
            if len(factors) > 2: # Can no longer be primes
                break # Stop current number. Saves time.
            x += 1

        if len(factors) == 2 and num not in primes:
            primes.append(num)
    # print(f'Primes leading up to {evenNum}:\n{primes}') #T#

    primePairList = []
    pairCount = 0
    if primes is not [] and evenNum >= 6:
        for elem in range(len(primes)):
            index = elem
            exceeded = False
            while not exceeded:
                while index < len(primes):
                    primeSum = primes[elem] + primes[index]
                    if primeSum > evenNum:
                        exceeded = True
                        break
                    elif primeSum == evenNum:
                        # primePairList.append([primes[elem], primes[index]])
                        pairCount += 1
                    index += 1
                break
        if primePairList is not [] and\
            evenNum % 1000 is 0:
            print(f'No. of prime pairs that form {evenNum}: {pairCount}')

if __name__ == '__main__':
    evenNum = 1000
    primes = []

    while True:
        genOddPrimes(evenNum)
        evenNum += 1000 # Next even number

