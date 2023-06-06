from random import randint as rand

money = 100
play = True
while play:
    fruits = ['cherry',
              'bell',
              'lemon',
              'orange',
              'star',
              'skull']

    go = input(f'You have {money}p. Roll? (Y/N) ').lower()
    if go == 'n':
        play = False
        break
    else:
        money -= 20
        print(f'Spent 20p. You now have {money}p.')

    choices = [fruits[rand(0,len(fruits)-1)] for x in range(3)]

    for choice in choices: print(choice)

    for choice in choices:
        if choices.count(choice) == 2:
            if choice != 'skull':
                money += 50
                print(f'You won 50p.')
            else:
                money -= 100
                print(f'You lost £1.')
            break

        elif choices.count(choice) == 3:
            if choice != 'skull':
                if choice == 'bell':
                    money += 500
                    print('You won £5.')
                else:
                    money += 100
                    print('You won £1.')
            else:
                money = 0
                print('Bankruptcy!')
            break
    print()
    if money <= 0:
        money = 0
        print('You\'ve lost all your money!\n')
        play = False

if __name__ == '__main__':
    if money == 0:
        print('You have nothing.')
    else:
        print(f'You finished with {money}p')