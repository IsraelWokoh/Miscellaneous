from string import ascii_uppercase as uppers, hexdigits

# TASK 1
# denary1 = int(input('Enter base-10 number: '))
# bits = ''
# while denary1 >= 1:
#     bits += str(denary1 % 2)
#     print(bits)
#     denary1//=2
# for bit in bits: print(bit, end='')

# TASK 2
# denary2 = int(input('\nEnter base-10 number: '))
# binary = ''
# while denary2 >= 1:
#     binary = str(denary2%2) + binary
#     # print(binary)
#     denary2 //= 2
# print(binary)

base10 = int(input('Enter base-10 number: '))
base16 = ''
hexDict = dict([[num, hexdigits[num]] for num in range(16)])
# print(hexDict)
while base10 >= 1:
    base16 = hexDict[base10%16] + base16
    base10 //= 16
print(base16.upper())
