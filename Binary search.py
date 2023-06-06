from random import randint

def binSearch(numbers, query):
    print(numbers)
    mid = len(numbers)//2 # Floor/integer division
    if numbers[mid] == query: # If median value
        return True
    elif len(numbers) != 1: # If there isn't only one element left
        if query > numbers[mid]:
            numbers = numbers[mid:]
        else:
            numbers = numbers[:mid]
        return binSearch(numbers, query)
    else:
        return False

evenNums = tuple(sorted(randint(1, 10000) for x in range(50)))
print(evenNums)
valid = False
while not valid:
    try:
        query = int(input('Enter number to search: '))
        valid = True
    except ValueError:
        print('Invalid entry.\n')


if binSearch(evenNums, query):
    print(f'{query} found.')  # Notify
else:
    print(f'{query} not found.')