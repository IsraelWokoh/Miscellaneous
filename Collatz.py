def collatz(x):
	steps = 0
	while x != 1:
		if not x%2:
			x //= 2
		else:
			x = 3*x+1
		steps += 1
	return steps


num = 0
while True:
	print(f'10^{num}: {collatz(10**num)} steps')
	num += 10000