#James Zhao
#Jan 27
#Period 7
#Magic 8 Ball


#Initialize
import random
import time
magic8list = ['It is certain', 'Yes definitely', 'Signs point to yes', 'You may rely on it', 'Outlook good',
              'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
              'Don’t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

#Functions
def playmagic8ball():
    print('Welcome to the magic 8 ball.')
    print('You ask a yes or no question and the magic 8 ball shall answer!')
    print('If you want to quit, please input "quit".\n')
    while True:
        question = input('What is your yes or no question? Type "quit" to quit.')
        if question.endswith('?'):
            for i in range(1,4):
                print('The magic 8 ball is being shaken' + '.'*i)
                time.sleep(0.75)
            magic_response = random.choice(magic8list)
            print('\n\nThe magic 8 ball says, "' + str(magic_response) + '!"')
            while True:
                play_again = input('Do you want to play again? (yes/no)')
                if play_again == 'yes':
                    print('\n\nPlaying again...\n\n')
                    playmagic8ball()
                    break
                elif play_again == 'no':
                    print('\n\nIt was fun playing magic 8 ball with you.\n\n.')
                    break
                else:
                    print('\n\nPlease input either "yes" or "no".\n\n')
            break
        elif question == 'quit':
            print('\n\nIt was fun playing magic 8 ball with you.\n\n')
            break
        else:
            print('\n\nYour question must end with a question mark!\n\n')

#Main
playmagic8ball()

