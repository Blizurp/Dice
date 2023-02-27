import random
#create dice
die1 = [1,2,3,4,5,6]
die2 = [1,2,3,4,5,6]

def roll():
    roll1 = random.choice(die1)
    roll2 = random.choice(die2)
    print('here comes the first roll')
    print(roll1)
    print('second die says:')
    print(roll2)
    print('together that makes:')
    print(roll1 + roll2)

print('hi welcome to the double die roller program!')
answer = input('would you like to roll the dice? (y/n)')
if answer == 'y':
    roll()
else:
    print('bye, bye')