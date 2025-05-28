#James Zhao
#Jan 27
#Period 7
#Slot Machine


#Initialize
import math
import random
import time
symbols = ['♥', '♦', '♠', '♣', '♠', '★'] * 3 + ['7'] * 7
chips = 0
wager = 0


#Functions
def get_emergency_fund():
    global chips
    print('You have ' + str(chips) + ' chips.')
    time.sleep(1)
    print('You do not have enough chips to wager anything!')
    while True:
        choice = input('Would you like to tap into your emergency funds to buy in for another 100 chips? (yes/no)')
        if choice == 'yes':
            chips += 100
            break
        elif choice == 'no':
            print('You leave the casino dejected.')
            break
        else:
            print('Please input "yes" or "no" to tap into your emergency funds.')

def wheel_spinning():
    global chips, symbols, wager
    print('\n\nYou put ' + str(wager) + ' chips into the machine...')
    time.sleep(1)
    random.shuffle(symbols)
    print('The wheel is spinning!')
    time.sleep(1)
    slot_1 = random.choice(symbols)
    slot_2 = random.choice(symbols)
    slot_3 = random.choice(symbols)
    print('The slots have stopped and reads as follows: ' + slot_1 + ' ' + slot_2 + ' ' + slot_3)

    if slot_1 == '7' and slot_2 == '7' and slot_3 == '7':
        print('CONGRATULATIONS! YOU HIT THE JACKPOT!!!')
        print('You are paid 10x your wager.\n\n')
        chips += (10 * wager)

    elif slot_1 == slot_2 and slot_2 == slot_3:
        print('Congratulations! You got 3 in a row!')
        print('You are paid 2.5x your wager.\n\n')
        chips += math.floor(2.5 * wager)

    elif slot_1 == slot_2 or slot_1 == slot_3 or slot_2 == slot_3:
        print('Congratulations! You got 2 of a kind!')
        print('You are paid 1.5x your wager.\n\n')
        chips += math.floor(1.5 * wager)

    else:
        print('Aw man. You hit nothing.\n\n')

def getting_wager():
    global chips, wager
    while True:
        print('You have ' + str(chips) + ' chips.')
        choice = input('Would you like to spin or quit?')
        if choice == 'spin':
            while chips > 0:
                try:
                    wager = input('How much would you like to wager?')
                    wager = int(wager)
                    if chips < wager:
                        print('\n\nYou only have ' + str(chips) + ' and cannot wager ' + str(wager) + ' chips.')
                        print('Please input a smaller wager.')

                    elif wager > 0:
                        chips -= wager
                        wheel_spinning()
                        break

                    else:
                        print('\n\nPlease input a positive integer amount of chips.')

                except ValueError:
                    print('\n\nPlease input a positive integer amount of chips.')

            if chips <= 0:
                get_emergency_fund()
                if chips <= 0:
                    break

        elif choice == 'quit':
            print('\n\nIt was fun playing slots with you!\n\n')
            break

        else:
            print('Please input either "spin" or "quit".\n\n')


def play_slot_machine():
    global chips
    print('Welcome to the slot machine!')
    print('There are 3 slots on the machine.')
    print('You decide how many chips to bet per spin.')
    print('Two of a kind gives a payback of 1.5x your wager.')
    print('3 in a row gives a payback of 2.5x your wager.')
    print("3 7's gives the jackpot of 10x your wager.\n\n")
    time.sleep(0.5)
    while True:
        try:
            chips = input('How many chips would you like to buy in for?')
            chips = int(chips)
            print('You bought in for ' + str(chips) + ' chips.\n\n')
            getting_wager()
            break

        except ValueError:
            print('Please input a positive integer amount of chips.')


#Main
play_slot_machine()
