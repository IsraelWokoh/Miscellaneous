def perfect(number, sumTotients = 0): # Determines if perfect totient
	if number == 1: # EXIT CASE
		# print(f'Totient: {sumTotients}')
		return totNumber == sumTotients # Boolean
	else:
		return perfect(
			totient(number),
			sumTotients + totient(number)
			)

def totient(number):
	# Set of all totatives. (Technically, doesn't need to be stored.)
	totatives = set(num for num in range(1, number) if gcd(number, num) == 1)
	return len(totatives)

def gcd(num1, num2): # Greatest Common Denominator
	if num2 > num1: # Ensures greater value first, then recurse
		return gcd(num2, num1)
	elif num1 == num2: # EXIT CASE 1
		return num1
	elif not num2: # EXIT CASE 2
		return num1
	else: # Recurse
		return gcd(num1%num2, num2)

if __name__ == '__main__':
	# totNumber = 1
	while True: # Infinite loop
		totNumber = int(input('\nEnter number: '))

		# PTN = perfect totient number
		if perfect(totNumber):
			print(f'{totNumber} is a PTN.')
		else:
			print(f'{totNumber} is NOT a PTN.')
		# totNumber += 1