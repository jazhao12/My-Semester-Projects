#James Zhao
#Jan 7
#Period 7
#Rock Paper Scissors


#Initialize
import random

#Functions
def play_rock_paper_scissors():
    player_win = 0
    player_tie = 0
    player_lose = 0
    print('Welcome to the game of Rock Paper Scissors!')
    print('In this game, rock beats scissors, scissors beats paper, and paper beats rock.')
    print('The person who beats the other wins this game.\n')
    print('You are now playing Rock Paper Scissors against the computer.\n')
    while True:
        intermediate_computer_choice = random.randint(1,3)
        if intermediate_computer_choice == 1:
            computer_choice = 'rock'
        elif intermediate_computer_choice == 2:
            computer_choice = 'paper'
        elif intermediate_computer_choice == 3:
            computer_choice = 'scissors'

        intermediate_player_choice = input('What would you like to play? (rock/paper/scissors)     Input "quit" to stop playing.')
        player_choice = intermediate_player_choice.lower()

        if player_choice == computer_choice:
            print('You have played ' + player_choice + ' and the computer has also played ' + computer_choice + '.')
            print('There is a tie!')
            player_tie += 1
            print('You have ' + str(player_win) + ' wins. The computer has ' + str(player_lose) + ' wins. There have been ' + str(player_tie) + ' ties.\n')

        elif player_choice == 'rock' and computer_choice == 'paper':
            print('You have played ' + player_choice + ' but the computer has played ' + computer_choice + '.')
            print('Paper beats rock and you lose.')
            player_lose += 1
            print('You have ' + str(player_win) + ' wins. The computer has ' + str(player_lose) + ' wins. There have been ' + str(player_tie) + ' ties.\n')

        elif player_choice == 'rock' and computer_choice == 'scissors':
            print('You have played ' + player_choice + ' and the computer has played ' + computer_choice + '.')
            print('Rock beats scissors and you win.')
            player_win += 1
            print('You have ' + str(player_win) + ' wins. The computer has ' + str(player_lose) + ' wins. There have been ' + str(player_tie) + ' ties.\n')

        elif player_choice == 'paper' and computer_choice == 'scissors':
            print('You have played ' + player_choice + ' but the computer has played ' + computer_choice + '.')
            print('Scissors beats paper and you lose.')
            player_lose += 1
            print('You have ' + str(player_win) + ' wins. The computer has ' + str(player_lose) + ' wins. There have been ' + str(player_tie) + ' ties.\n')

        elif player_choice == 'paper' and computer_choice == 'rock':
            print('You have played ' + player_choice + ' and the computer has played ' + computer_choice + '.')
            print('Paper beats rock and you win.')
            player_win += 1
            print('You have ' + str(player_win) + ' wins. The computer has ' + str(player_lose) + ' wins. There have been ' + str(player_tie) + ' ties.\n')

        elif player_choice == 'scissors' and computer_choice == 'rock':
            print('You have played ' + player_choice + ' but the computer has played ' + computer_choice + '.')
            print('Rock beats scissors and you lose.')
            player_lose += 1
            print('You have ' + str(player_win) + ' wins. The computer has ' + str(player_lose) + ' wins. There have been ' + str(player_tie) + ' ties.\n')

        elif player_choice == 'scissors' and computer_choice == 'paper':
            print('You have played ' + player_choice + ' and the computer has played ' + computer_choice + '.')
            print('Scissors beats paper and you win.')
            player_win += 1
            print('You have ' + str(player_win) + ' wins. The computer has ' + str(player_lose) + ' wins. There have been ' + str(player_tie) + ' ties.\n')

        elif player_choice == 'quit':
            print('Thanks for playing Rock Paper Scissors with the computer.')
            break

        else:
            print('Please input "rock", "paper", "scissors", or "quit".\n')

#Main
play_rock_paper_scissors()
