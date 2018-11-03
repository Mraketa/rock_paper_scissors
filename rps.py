import random

def input_human_play():
    play = input('rock, paper or scissors? ')
    while not is_valid_play(play):
        play = input('rock, paper or scissors? ')
    return play
    
def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']

def generate_computer_play():
    return random.choice(['rock', 'paper', 'scissors'])

def evaluate_game(human, computer):
    if human == computer:
        return 'tie'
    elif (human == 'rock' and computer == 'scissors') or (human == 'scissors' and computer == 'paper') or (human == 'paper' and computer == 'rock') :
        return 'human'
    elif (human == 'rock' and computer == 'paper') or (human == 'scissors' and computer == 'rock') or (human == 'paper' and computer == 'scissors') :
        return 'computer'

# ------

def main():
    human = input_human_play()
    computer = generate_computer_play()

    print('Computer plays: ', computer)
    game = evaluate_game(human, computer)
    if game == 'tie':
        print ('it\'s a tie!')
    else:
        print(f'{game} won')
        
if __name__ == '__main__':
    main()
    
    
    
    
    
    


    # if human == computer:
        # print('it\'s a tie!')
    # elif (human == 'rock' and computer == 'scissors') or (human == 'scissors' and computer == 'paper') or (human == 'paper' and computer == 'rock') :
        # print('Human wins!')
    # elif (human == 'rock' and computer == 'paper') or (human == 'scissors' and computer == 'rock') or (human == 'paper' and computer == 'scissors') :
        # print('Computer wins!')