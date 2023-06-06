from math import floor, sqrt

def factorise(num):
    factors = []
    x = 1 # Incremented factor

    while x <= sqrt(num):   # Square root not reached
        if num % 2 == 1 and x % 2 == 0: # if num odd and x is even
            pass # ...don't bother

        elif num % x == 0: # If a factor
            if x not in factors: # If factor not already stored
                factors.append(x) # Store
            if int(num/x) not in factors: # If corresponding factor not stored
                factors.append(int(num/x)) # Store
        x += 1
    if num != 1 and len(factors) != 2:
        print(f'{num} has {len(factors)} factors.\n') # Prints number of factors
    elif num == 1:
        print("1 only has one factor.\n")
    else:
        print(f'{num} is prime.\n')
    return sorted(factors)

def showFactors(facs):
    for fac in facs:
        if facs.index(fac) % 6 == 5:
            print(fac)
        else:
            print(fac, end = " ")
    print()

if __name__ == '__main__':
    while True:
        factorList = factorise(int(input("Enter number to factorise: ")))
        showFactors(factorList)