from time import time
from random import randint

def sumDigits(number):
    number = sum([int(char) for char in str(number)])
    if len(str(number)) != 1: return sumDigits(number)
    return number

for times in range(10):
    num = ''
    for x in range(10**6): # million-digit number
        num += str(randint(0,9))
    #print(num)
    print(sumDigits(num))



begin = 1
stop = 1000000
print(stop-begin+1)
start = time()
for x in range(begin,stop+1):
    sumDigits(x)
end = time()
print(f'Done! Took {end-start} secs\n\
{round((stop-begin+1)/(end-start),2)} numbers/sec')
