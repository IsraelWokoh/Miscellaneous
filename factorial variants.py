from functools import reduce
from operator import mul
from math import log10
from time import time

def fac1(k = int()):
	return 1 if k in [0,1] else k*fac1(k-1)

def fac2(n, a = int()):
	if not n: return 1
	if not a: a=n-1 if n else n
	return n if a in {0,1} else fac2(n*a, a-1)

def fac3(n, a = int()):
	if not n: return 1
	if not a:
		if n:
			a = n-1
		else:
			a = n
	if a in {0,1}:
		return n
	else:
		return fac3(n*a, a-1)

def fac4(q = int()):
	total = 1
	for num in range(1, q+1):
		total *= num
	return total

def fac5(r = int()):
	return reduce(mul, range(1,r+1), 1)

if __name__ == '__main__':
	for func in {fac1, fac2, fac3, fac4, fac5}:
		# print(func(int(input('enter: '))))
		x = 0
		start = time()
		for x in range(1000):
			# x = int(input('Enter number: '))
			# if not x % 100:
			# 	print(x)
			try:
				fac = func(x)
			except RecursionError:
				print('Recursion error!\n')
				break
			# else:
			# 	print(f'Digits in {x}!: {int(log10(fac)+1)}\n')
		end = time()
		print(f'Done in {round(end-start,6)} secs!\n')