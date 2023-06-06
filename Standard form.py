from random import randint

def std(num):
    exp = 0
    while not abs(num) < 10:
        num /= 10
        exp += 1
    print(f'{round(num,3)} ⋅ 10^{exp}')

for count in range(20):
    number = randint(1, 10 ** 4)
    print(f'{number} = ', end = '')
    std(number)