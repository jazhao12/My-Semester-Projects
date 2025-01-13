#James Zhao
#Nov 8
#Period 7
#Number Guesser Script


#Initialize
import random
playerPoints = int(0)

#Functions
def runNumberGuesser():
    global playerPoints
    print('Welcome to Random Number Guesser, the game where you try to guess the randomly generated number!')
    print('You will gain one point if you win easy, two for medium, and five for hard.')
    print('You will not lose any points if you lose a round.')
    difficulty = input('What difficulty do you want to play? (easy/medium/hard)')

    if difficulty == 'easy':
        secret = random.randint(1,10)
        lives = 10
        print('You have chosen easy. You have ten lives and your numbers range from 1-10, inclusive.')
        while lives > 0:
            guess = int(input('What is your number? (1-10)'))
            if guess == secret:
                lives -=1
                print('Congratulations! You guessed the correct number!')
                playerPoints += 1
                playAgain()
                break
            elif guess < secret:
                lives -=1
                print('Your guess of ' + str(guess) + ' was too low. You have ' + str(lives) + ' lives left.')
            elif guess > secret:
                lives -=1
                print('Your guess of ' + str(guess) + ' was too high. You have ' + str(lives) + ' lives left.')
            else:
                print('Please input a guess in the form of an integer. Tip: Your guess should be written the provided range!')
        else:
            print('You have run out of lives. The correct number was ' + str(secret) + '.')
            playAgain()

    elif difficulty == 'medium':
        secret = random.randint(1,50)
        lives = 5
        print('You have chosen medium. You have five lives and your numbers range from 1-50, inclusive.')
        while lives > 0:
            guess = int(input('What is your number? (1-50)'))
            if guess == secret:
                lives -=1
                print('Congratulations! You guessed the correct number!')
                playerPoints += 2
                playAgain()
                break
            elif guess < secret:
                lives -=1
                print('Your guess of ' + str(guess) + ' was too low. You have ' + str(lives) + ' lives left.')
            elif guess > secret:
                lives -=1
                print('Your guess of ' + str(guess) + ' was too high. You have ' + str(lives) + ' lives left.')
            else:
                print('Please input a guess in the form of an integer. Tip: Your guess should be written the provided range!')
        else:
            print('You have run out of lives. The correct number was ' + str(secret) + '.')
            playAgain()

    elif difficulty == 'hard':
        secret = random.randint(1,100)
        lives = 3
        print('You have chosen hard. You have three lives and your numbers range from 1-100, inclusive.')
        while lives > 0:
            guess = int(input('What is your number? (1-100)'))
            if guess == secret:
                lives -=1
                print('Congratulations! You guessed the correct number!')
                playerPoints += 5
                playAgain()
                break
            elif guess < secret:
                lives -=1
                print('Your guess of ' + str(guess) + ' was too low. You have ' + str(lives) + ' lives left.')
            elif guess > secret:
                lives -=1
                print('Your guess of ' + str(guess) + ' was too high. You have ' + str(lives) + ' lives left.')
            else:
                print('Please input a guess in the form of an integer. Tip: Your guess should be written the provided range!')
        else:
            print('You have run out of lives. The correct number was ' + str(secret) + '.')
            playAgain()

def playAgain():
    global playerPoints
    while True:
        print('You ended this round with ' + str(playerPoints) + ' points.')
        play = str(input('Would you like to play again? (yes/no)'))
        if play == 'yes':
            runNumberGuesser()
            break
        elif play == 'no':
            print('It was fun playing with you!')
            quit(0)
            break
        else:
            print('Please input either "yes" or "no".')
#Main
runNumberGuesser()
