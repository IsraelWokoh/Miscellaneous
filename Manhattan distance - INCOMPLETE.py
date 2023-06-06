from math import sqrt, ceil, floor

def calcDist(num):
    currentIndex = ceil(sqrt(num))**2 # Finds next highest square number
    minDist = int(floor(sqrt(peakSquare) / 2)) # Calculate lowest dist in group
    maxDist = int(2 * minDist) # Calculate highest dist in group
    currentDist = int(sqrt(currentIndex) - 1)
    return minDist, maxDist, currentDist, currentIndex
    
def distFrom1(num):
    if sqrt(num) % 1 == 0: # If square number
        return int(sqrt(num)) - 1
    
    else: # Not a perfect square
        minDist, maxDist, currentDist, currentIndex = calcDist(num)
        print('minDist:', minDist, '--', 'maxDist:', maxDist) #T#

        indexDist = [currentIndex, currentDist] #T#
        print('indexDist', indexDist)

        if currentDist != minDist:
            while currentDist > minDist:
                currentIndex -= 1
                currentDist -= 1
                if currentIndex == num:
                    print(currentIndex, currentDist)
                    return currentDist
            indexDist = [currentIndex, currentDist]
            print('new indexDist:', indexDist) #T#
        
        else:
            while currentDist < maxDist:
                currentIndex -= 1
                currentDist += 1
                if currentIndex == num:
                    print(currentIndex, currentDist)
                    return currentDist
        

if __name__ == '__main__':
    numVal = False
    while not numVal:
        try:
            num = int(input('Enter number: '))
            if num > 0:
                numVal = True
            else:
                print('Please enter a non-zero, positive integer.\n')
        except ValueError:
            print('Please enter a valid NUMBER.\n')
    print('Distance from centre:', distFrom1(num))

'''
STEPS
find ceil square - thus first = last value (refer to PATTERNS)
find min and max values
    min: floor(sqrt+1/2)
    max: 2*min
find start
    start = sqrt - 1
    start -> min -> max -> min -> start - SYMMETRY
'''

'''
PATTERNS
odd: even
even: odd
when grouping into square numbers (refer to picture taken)
min values: 0, 1, 1, 2, 2, 3, 3...
max values: 0, 2, 2, 4, 4, 6, 6...
start value = last value: 0, 1, 2, 3, 4, 5, 6...
square: sqrt(square) - 1
square + 1: sqrt(square)
start -> min -> max -> min -> start - SYMMETRY
That should be enough information.
'''
