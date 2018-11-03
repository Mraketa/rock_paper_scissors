import random

human = input('rock, paper of scissors? ')

while human not in ['rock', 'paper', 'scissors']:
    human = input('rock, paper of scissors?')
    
computer = random.choice(['rock', 'paper', 'scissors'])

print('Computer plays: ', computer)

if human == computer:
    print('it\'s a tie!')
elif (human == 'rock' and computer == 'scissors') or (human == 'scissors' and computer == 'paper') or (human == 'paper' and computer == 'rock') :
    print('Human wins!')
elif (human == 'rock' and computer == 'paper') or (human == 'scissors' and computer == 'rock') or (human == 'paper' and computer == 'scissors') :
	print('Computer wins!')