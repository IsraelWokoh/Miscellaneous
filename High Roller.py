from random import randint as rand, shuffle

players = []
numTry = False
while not numTry:
    try:
        numPlayers = int(input('How many players? (1-4) '))
        if 1 <= numPlayers <= 4:
            numTry = True
        else:
            print('Number of players must be between 1 and 4.\n')
    except ValueError:
        print('Enter a whole number, please.\n')

for x in range(numPlayers):
    players.append([input(f'Enter Player {x+1}\'s name: ').title(), 0, 0])
print()

if len(players) is 1:
    print('You\'ll need to play the CPU.')
    players.append(['CPU', 0, 0])


shuffle(players)

index = 0
play = True
while play:
    index %= len(players)
    name = 0
    score = 1
    old = 2
    new = rand(1,6)
    players[index][score] += new

    if new is players[index][old]:
        print(f'Double points for you, {players[index][name]}!')
        players[index][score] += new
    print(f'{players[index][name]}, you rolled a {new}. \
{players[index][name]}\'s score is now {players[index][score]}')

    buffer = input('Press ENTER to continue\n')

    if players[index][score] >= 30:
        break

    players[index][old] = new # Replace old score
    index += 1

print(f'{players[index][name]} wins!')