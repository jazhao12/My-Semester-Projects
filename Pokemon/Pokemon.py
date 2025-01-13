#James Zhao
#Nov 20
#Period 7
#Pokemon Evolution Game


#Initialize
import random
import sys
import time
pokemon_level = 0
pokemon_name = 'Igglybuff'
player_gym_wins = 0
player_gym_losses = 0
player_elite4_wins = 0
player_elite4_losses = 0
save_file = "pokemon_game_save.txt"
day = 1
special_pokemon_chance = 0.05
special_pokemon_battle = 0

#Functions
def waiting_animation():
    for i in range(4):
        print('.'*i)
        time.sleep(0.75)

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def draw_igglybuff():
    print('''
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠒⠂⠉⠒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⢀⣱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⠒⠚⣄⠀⠀⠀⢠⠖⠉⠀⠈⠑⢦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠈⠁⠀⠀⠀⠁⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡣⠤⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠈⠁⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢅⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠔⠋⠀⢠⠴⣛⣉⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢢⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⢀⡇⣞⠉⡄⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢆⠀⠀⠀
⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠈⣦⡈⠋⢁⡴⠃⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀
⠀⠀⠀⢠⠃⡠⠺⡖⠆⠀⠀⠀⠉⠉⠉⠀⢀⠔⠋⢳⣤⣌⠑⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠀
⠀⠀⠀⠏⣼⣁⣴⣿⢾⠀⠀⠀⠀⠀⠀⠀⠸⢦⣠⣾⣿⣿⣷⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀
⠀⠀⢰⠀⡇⣿⡿⡿⡨⠀⠀⠀⠀⠀⠀⠀⢠⠈⢿⣿⣿⢟⠏⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇
⠀⠀⢸⠀⢧⠘⢛⣡⠃⢀⠀⠀⠀⢀⠀⠀⠀⠳⢄⡉⠉⢁⡠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⢀⡠⢼⡀⠀⠙⠉⠁⠀⠈⠙⡉⠉⣁⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠒⠉⠉⠁⠈⡇⠀⠀⠀⠀⠀⡞
⠘⢦⡀⣇⠀⠀⠀⠀⠀⠀⠀⠳⣩⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠀⠀⠀⠀⠀⢠⠇
⠀⠀⠈⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠉⠀⠀⠀⠀⠀⠀⠀⡞⠀
⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀
⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠒⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠉⠑⠀⢰⠆⠀⠀⠐⠐⡖⠉⠀⠀⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⡠⠂⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠒⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⢄⣀⡐⠀⠀⠀⠀⠀⠀⠀⠀''')

def draw_jigglypuff():
    print('''
          ⢀⣀⣀⡠⠖⢉⣌⢆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠚⠉⠀⠈⠉⠲⣿⣿⡜⡀⠀⠀⠀⠀
⡔⢉⣙⣓⣒⡲⠮⡇⠀⠀⠀⠀⠀⠀⠘⡿⡇⡇⠀⠀⠀⠀
⡇⠘⣿⣿⣿⠏⠀⠀⠠⣀⡀⠀⠀⠀⠀⡇⠈⠳⡄⠀⠀⠀
⢹⠀⢻⣿⠇⠀⠀⣀⣀⠀⡍⠃⠀⠀⣠⣷⡟⢳⡜⡄⠀⠀
⠈⣆⠀⠋⢀⢔⣵⣿⠋⠹⣿⠒⠒⠚⠁⣿⣿⣾⣷⢸⠤⡄
⠀⡇⠀⠀⢸⢸⣿⣿⣶⣾⡏⡇⠀⠀⢀⡘⣝⠿⡻⢸⡰⠁
⠀⢳⠀⠀⠈⢆⠻⢿⡿⠟⡱⠁⠰⠛⢿⡇⠀⠉⠀⡸⠁⠀
⠀⠈⢆⠀⠀⠀⠉⠒⠒⣉⡀⠀⠀⢇⠀⡇⠀⠀⢠⠃⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠀⠀⠀⢉⡱⠀⠀⠉⠀⢀⡴⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠓⠦⣀⣉⡉⠁⢀⣀⣠⠤⠒⠥⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⣉⣀⣀⡠⠭⠛⠀⠀⠑⠒⠤⠤⠷⠀⠀⠀''')

def draw_wigglytuff():
    print('''
 ⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⢹⠀⠀
⢸⠀⠤⣈⡁⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠔⢁⠄⢸⠀⠀
⠀⢆⠀⢸⣿⣷⣦⣌⠑⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠤⠠⠤⣀⠀⠀⠀⠀⡴⠁⣰⣿⠀⣸⠀⠀
⠀⠈⢆⠈⢧⠉⠹⣿⣿⣦⡈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠘⠀⢀⠀⠀⠀⠑⢦⣀⠎⢀⣾⣿⡏⢀⠇⠀⠀
⠀⠀⠀⠡⡀⠑⢄⠘⣿⣿⣿⣦⡘⢦⠀⠀⣀⠤⠤⢰⠿⢄⣀⡗⠀⠀⠀⠀⢩⢠⣿⣿⡿⠀⡘⠀⠀⠀
⠀⠀⠀⠀⠈⠂⢄⠑⠻⣿⣿⣿⣷⡄⢳⠉⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⡿⠁⡰⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠑⠢⠬⣙⠻⠿⡿⠂⠂⠀⠀⠀⠘⣄⠀⠀⠀⠀⠀⠀⢀⡜⠻⣎⡠⠚⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⠑⠒⠀⠀⢀⠤⢒⣒⣌⡓⠤⢄⣀⠠⠔⢫⣖⡢⡙⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠁⠀⠀⠀⠀⡰⠁⣼⠁⡿⠏⢳⡀⠀⠀⠀⠀⢸⣍⡟⡌⢿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠇⠀⡇⠉⠁⠀⣸⠇⠀⠀⠀⠀⠈⣧⠥⣼⠈⢣⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠘⢄⡐⠄⣀⣵⠟⠀⣀⠀⠀⠀⢀⠈⠳⠯⠂⠘⡆⠀⣀⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡜⠠⠒⠂⠐⠒⠢⢄⠀⠀⠀⠀⠀⠀⠀⠘⠂⠤⠒⠁⠀⠀⠀⠀⠀⢹⠁⠀⠀⡸
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠘⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⢀⡴⠁
⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠑⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡗⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡘⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢰⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⡀⠀⠰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⣤⣀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣊⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⠉⠑⢲⠀⠀⠀⠀⠀⠀⠴⣒⠉⠁⠀⠀⠀⠈⢳⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠈⠙⠒⠤⠤⠠⠤⠊⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠦⣀⡀⣀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

def draw_zorua():
    print('''
          ⠀⠀⠀⠀⠀⠀⠀⠀ ⡼⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⠠⢄⡀⠀⠀⠀⠀⠀⠀⢀⡤⡄⢀⠔⠁⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡇⠀⠀⠉⠢⣀⠀⢀⡤⠚⠁⠼⠛⠁⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⡀⠀⠀⠀
⠀⡇⠀⠀⠀⠀⢀⠝⢁⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⢹⠀⠀⠀⢀⡤⠖⠊⠁⠀⠀⠀⡏⢠⢲⡀
⠀⡇⠀⢱⣤⣰⠃⢠⠏⠀⠀⠀⠀⠀⣀⡤⠚⢹⠐⠀⣞⡠⠔⠈⠁⠀⠀⢀⡀⠀⠀⢸⢁⠇⠀⣇
⠀⢱⠀⢸⣿⡇⢀⣾⠀⠀⠀⣠⠖⠋⠁⠀⠀⡼⢀⣴⡏⠀⠀⢀⣠⣴⣾⣿⠁⠀⢠⠟⡿⠀⠀⣿
⠀⠘⡄⠸⡟⣧⡏⢸⡠⠀⡰⠁⠀⠀⠀⠀⣴⠕⠋⡸⠀⣀⣴⣿⣿⡿⣻⠃⠀⠀⡌⠀⢳⠀⠀⢸
⠀⠀⢃⠀⢷⡽⣅⠈⢷⣄⡇⠀⠀⠀⠀⠀⠀⢀⡴⠁⠘⢻⣿⣿⠋⣰⠃⠀⠀⣼⡁⠀⢸⠀⠀⢸
⠀⠀⠘⡄⠸⠁⠙⠢⣄⡈⠁⠀⠀⠀⠀⣀⡤⠊⠀⠀⠀⠀⠙⣆⣰⠃⠀⠀⣜⣙⣥⣤⢼⡤⠀⢸
⠀⠀⠀⢱⠃⣀⡀⢀⡀⠁⢀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⢀⣼⣿⣿⣏⣠⠞⠀⠀⣸
⢪⠒⠤⣸⣸⠠⢱⣾⢸⠀⠀⠀⡰⠋⢧⢀⠔⠚⠓⢆⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⠑⠀⠀⢠⡇
⠀⠱⡄⠈⣿⢣⡀⣿⠞⠀⠀⠀⣇⢇⣾⡎⠀⢀⣠⠾⡆⠀⢀⣀⠤⠜⠛⠛⠉⠉⣩⢝⠁⢀⡞⠀
⠀⠠⣬⣦⣘⣾⡹⢾⠀⠀⠀⠀⠈⠉⢸⣰⣴⡟⢹⢀⡇⠀⠈⠀⠀⠀⢀⣠⣴⡾⠇⢀⣠⠞⠀⠀
⠀⠀⠈⠢⢍⡛⢝⡾⠃⠀⠀⠀⠀⠀⠘⣇⠙⢃⡎⡸⠁⠀⠠⠤⠶⢾⣿⣿⣿⡇⢸⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⡝⠀⠀⠀⠀⠀⠀⠀⠀⠘⠫⠥⢾⠅⣀⣴⣶⣶⣾⣿⣿⠿⡿⠀⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠳⠤⣀⣀⣀⣀⣀⣀⣀⣠⣴⣿⣿⣿⣿⣿⣿⡿⠋⠁⡼⠁⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⣠⠾⡧⠤⢴⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠙⠿⣿⣿⣿⣿⣿⣿⣿⣥⠴⠊⠀⠀⢇⣀⡜⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠉⡏⠉⠉⠉⢉⡃⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠚⣇⠀⠀⢀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠍⠋⡹⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

def draw_zoroark():
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡆⢀⠜⡟⠀⠀⠀⠀⠀⠀⠀⣀⠤⣺⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⢻⠗⠛⠙⠃⠉⠉⢉⠴⣶⠖⠋⢁⣴⡃⠀⠀⠀⠀⠀⢀⣀⢤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⢧⠀⢀⠴⠺⠷⣻⠀⠀⠀⠀⠀⠀⠀⠴⠛⣿⠶⠋⠀⠈⠉⠩⢽⣉⠉⣁⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣨⡖⠁⠀⠀⠀⠋⠀⡀⠀⠀⠀⠀⠀⠐⠋⠁⠀⠀⠀⠀⠀⠠⠔⠛⢯⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡜⠁⣷⠀⠀⢀⡤⣺⠏⠇⠀⠀⠀⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢤⣄⣙⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⢀⡴⣫⣾⡜⣼⠀⣀⣴⡟⢽⠁⠀⠀⠀⠀⠀⠀⠀⠠⣔⠈⠙⠳⣤⣉⣀⠙⠢⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣰⠀⣀⣶⣿⠄⠀⢛⣾⣷⡿⠫⡟⠀⢸⡆⠀⠀⠀⣀⣶⣴⣆⣤⣶⣾⣷⣶⣿⡇⠀⠉⠉⠉⠛⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣿⡿⣿⣾⡿⣸⡇⢸⣿⡟⠁⠘⢷⣾⠟⠛⢚⣳⠞⠋⠈⠉⠴⢾⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⢉⣀⣈⠤⢾⣿⣿⣿⡿⠀⠀⠀⠊⣻⠟⠋⠉⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠈⣿⣿⣿⠁⠀⠀⢠⢾⢀⣦⡄⢀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢜⡴⠋⠛⠛⠿⠿⣷⣿⣿⡽⠻⡍⠛⠓⠚⠛⠻⠿⢿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡠⠔⠒⠉⠉⠥⣮⣿⠁⠀⠀⠀⠀⠈⠉⣻⠀⠀⠈⢷⠤⣀⠀⠀⠀⠀⣸⠻⠿⡋⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡠⢖⡯⣄⠀⢀⡤⠖⠉⠀⠀⠀⠀⠀⠀⢀⡠⠴⢹⣧⣀⢻⡛⠷⣈⠙⠢⡀⢠⣿⣤⣤⣴⣿⣿⣿⣿⣿⣧⣀⠀⠀⠀⠀⢠⡀
⠛⣺⣹⢾⡡⠓⠉⠀⠀⠀⠀⠀⠀⡠⠔⠊⠁⠀⠀⠋⡇⢻⡷⢷⡀⠈⣳⠀⠈⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡿⣒⡒⠒⡹⠁
⠀⠉⠀⠉⠀⠀⠀⠀⠀⠀⠀⡴⢊⠀⠀⠀⠀⠀⠀⠀⠱⣄⠳⣄⠁⠈⠐⡀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢱⠀⣠⠞⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⢇⡠⠤⠤⣔⠒⠀⠈⠉⠉⠉⠘⢢⡀⠀⠀⠢⡀⠀⠹⣿⣿⣿⣿⣿⡿⠟⠉⣠⡤⠚⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠉⢳⠀⠀⠀⠀⠀⠀⠙⢄⠀⠀⠘⠀⠀⠷⠚⢯⡉⠙⠓⠈⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠞⡲⠐⠆⡾⠀⠀⠀⠀⠀⠀⠀⠀⠣⣄⣄⠈⢰⣤⣀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣶⣟⡻⠲⣤⠔⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠈⡀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠧⣡⣬⣡⢬⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣮⠶⠛⣸⠻⣔⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀''')

def train():
    global pokemon_level
    delay_print(str(pokemon_name) + ' is currently level ' + str(pokemon_level) + '.')
    time.sleep(0.5)
    delay_print('\nYou have begun training ' + str(pokemon_name) + '.\n')
    waiting_animation()
    pokemon_level += 1
    delay_print("\nCongratulations! " + str(pokemon_name) +  " is now level " + str(pokemon_level) + '.')
    evolve_pokemon()

def evolve_pokemon():
    global pokemon_level, pokemon_name, special_pokemon_battle
    different_evolution = random.randint(1,100)
    if pokemon_level >= 5 and pokemon_name == 'Igglybuff' and different_evolution > special_pokemon_chance:
        time.sleep(1.5)
        delay_print("\n\nWhat's this?")
        time.sleep(1.5)
        delay_print('\nIgglybuff is evolving!\n')
        waiting_animation()
        delay_print("\nCongratulations! Your Igglybuff evolved into Jigglypuff!\n")
        pokemon_name = 'Jigglypuff'
    elif pokemon_level >= 5 and pokemon_name == 'Igglybuff' and different_evolution <= special_pokemon_chance:
        time.sleep(1.5)
        delay_print("\n\nWhat's this?")
        time.sleep(1.5)
        delay_print('\nIgglybuff is attempting to evolve!\n')
        waiting_animation()
        delay_print("\nWoah!)")
        time.sleep(1)
        delay_print("Your Igglybuff was secretly Zorua!\n")
        pokemon_name = 'Zorua'
        special_pokemon_battle = 5
    elif pokemon_level >= 10 and pokemon_name == 'Jigglypuff' and different_evolution > special_pokemon_chance:
        time.sleep(1.5)
        delay_print("\nWhat's this?")
        time.sleep(1.5)
        print('\nJigglypuff is evolving!')
        waiting_animation()
        print("\nCongratulations! Your Jigglypuff evolved into Wigglytuff!\n")
        pokemon_name = 'Wigglytuff'
    elif pokemon_level >= 10 and pokemon_name == 'Jigglypuff' and different_evolution <= 0.4*special_pokemon_chance:
        time.sleep(1.5)
        delay_print("\nWhat's this?")
        time.sleep(1.5)
        print('\nJigglypuff is attempting to evolve!')
        waiting_animation()
        delay_print("\nWoah!)")
        time.sleep(1)
        delay_print("Your Jigglybuff was secretly Zoroark!\n")
        pokemon_name = 'Zoroark'
        special_pokemon_battle = 10
    elif pokemon_level >= 30 and pokemon_name == 'Zorua':
        time.sleep(1.5)
        delay_print("\nWhat's this?")
        time.sleep(1.5)
        print('\nZorua is evolving!')
        waiting_animation()
        print("\nCongratulations! Your Zorua evolved into Zoroark!\n")
        pokemon_name = 'Zoroark'
        special_pokemon_battle = 10
    time.sleep(1.5)

def fight_gym():
    global pokemon_level, pokemon_name, player_gym_wins, player_gym_losses
    delay_print('You have gone to your local pokemon gym to fight...\n')
    waiting_animation()
    successful_battle = random.randint(1,1000)
    if successful_battle%2 == 1:
        delay_print("\nCongratulations! You have returned victorious!")
        player_gym_wins += 1
        pokemon_level += 2
        delay_print('\n' + str(pokemon_name) +  ' is now level ' + str(pokemon_level) + '.')
        time.sleep(1.5)
        evolve_pokemon()
    elif successful_battle%2 == 0:
        player_gym_losses += 1
        delay_print('\nUnfortunate. The trainers there were too strong.\n')
        time.sleep(1.5)

def fight_elite_four():
    global pokemon_level, player_elite4_wins, player_elite4_losses, special_pokemon_battle
    delay_print('\nYou have dared to challenge the Elite Four.')
    time.sleep(2)
    delay_print('\nYou are now fighting Elite Four Will...\n')
    waiting_animation()
    successful_battle1 = random.randint(1,100)
    if successful_battle1 > (50-0.5*pokemon_level-special_pokemon_battle):
        delay_print('You have defeated Elite Four Will. ')
        time.sleep(1)
        delay_print('Three trainers now stand in your way of becoming the best trainer.')
        time.sleep(1.75)
        delay_print('\nYou are now fighting Elite Four Koga...\n')
        waiting_animation()
        successful_battle2 = random.randint(1,100)
        if successful_battle2 > (56-0.4*pokemon_level-special_pokemon_battle):
            delay_print('You have defeated Elite Four Koga. ')
            time.sleep(1)
            delay_print('Two more trainers now stand in your way of becoming the best trainer.')
            time.sleep(1.75)
            delay_print('\nYou are now fighting Elite Four Bruno...\n')
            waiting_animation()
            successful_battle3 = random.randint(1,100)
            if successful_battle3 > (60-0.3*pokemon_level-special_pokemon_battle):
                delay_print('You have defeated Elite Four Bruno. ')
                time.sleep(1)
                delay_print('Only one trainer now stands in your way of becoming the best trainer.')
                time.sleep(1.75)
                delay_print('\nYou are now fighting Elite Four Karen...\n')
                waiting_animation()
                successful_battle4 = random.randint(1,100)
                if successful_battle4 > (62-0.2*pokemon_level-special_pokemon_battle):
                    player_elite4_wins += 1
                    delay_print('What an accomplishment!\n')
                    time.sleep(2)
                    delay_print('You have beaten the Elite Four!\n')
                    time.sleep(2)
                    delay_print('You are the best trainer in the world!\n')
                    time.sleep(4)
                else:
                    player_elite4_losses += 1
                    delay_print('\nYou were too bold and have been defeated.\n')
                    time.sleep(3)
            else:
                player_elite4_losses += 1
                delay_print('\nYou were too bold and have been defeated.\n')
                time.sleep(3)
        else:
            player_elite4_losses += 1
            delay_print('\nYou were too bold and have been defeated.\n')
            time.sleep(3)
    else:
        player_elite4_losses += 1
        delay_print('\nYou were too bold and have been defeated.\n')
        time.sleep(3)

def display_pokemon():
    if pokemon_name == 'Igglybuff':
        draw_igglybuff()
        print('\n\nYou have an Igglybuff!')
    elif pokemon_name == 'Jigglypuff':
        draw_jigglypuff()
        print('\n\nYou have a Jigglypuff!')
    elif pokemon_name == 'Wigglytuff':
        draw_wigglytuff()
        print('\n\nYou have a Wigglytuff!')
    elif pokemon_name == 'Zorua':
        draw_zorua()
        print('\n\nYou have a Zoroark')
    elif pokemon_name == 'Wigglytuff':
        draw_zoroark()
        print('\n\nYou have a Zoroark!')
    print(str(pokemon_name) + ' is currently level ' + str(pokemon_level) + '.')
    print('\nLocal Pokemon Gym:')
    print('Wins: ' + str(player_gym_wins))
    print('Losses: ' + str(player_gym_losses))
    print('\nElite Four: ')
    print('Wins: ' + str(player_elite4_wins))
    print('Losses: ' + str(player_elite4_losses))
    time.sleep(5)

def save_game():
    while True:
        save_double_check = input('Do you want to save the game? (y/n)')
        if save_double_check == 'y':
            with open(save_file, "w") as file:
                file.write(pokemon_name + "\n")
                file.write(str(pokemon_level) + "\n")
                file.write(str(player_gym_wins) + "\n")
                file.write(str(player_gym_losses) + "\n")
                file.write(str(player_elite4_wins) + "\n")
                file.write(str(player_elite4_losses) + "\n")
                file.write(str(day) + "\n")
            for i in range(1,4,1):
                print('Saving the game' + '.'*i)
                time.sleep(0.75)
            delay_print("Game saved successfully!\n")
            break
        elif save_double_check == 'n':
            break
        else:
            print('Please enter "y" or "n" to save or not save the game.')

def load_game():
    global pokemon_name, pokemon_level, player_gym_wins, player_gym_losses, player_elite4_wins, player_elite4_losses, day
    while True:
        load_double_check = input('Do you want to load the save file? (y/n)')
        if load_double_check == 'y':
            try:
                with open(save_file, "r") as file:
                    pokemon_name = file.readline().strip()
                    pokemon_level = int(file.readline().strip())
                    player_gym_wins = int(file.readline().strip())
                    player_gym_losses = int(file.readline().strip())
                    player_elite4_wins = int(file.readline().strip())
                    player_elite4_losses = int(file.readline().strip())
                    day = int(file.readline().strip())
                for i in range(1,4,1):
                    print('Loading the game' + '.'*i)
                    time.sleep(0.75)
                print("Game loaded successfully!")
                break
            except FileNotFoundError:
                print("No save file found. Please start and save a new game.")
                break
            except ValueError:
                print("Save file is corrupted. Unfortunately, you must start a new game.")
                break
        elif load_double_check == 'n':
            break
        else:
            print('Please enter "y" or "n" to load or not load the game.')

def pokemon_game():
    global day
    print('Welcome to Pokemon Evolution Simulator!')
    while True:
        print('\nChoose an activity to do for the day. It is currently day ' + str(day) + '.')
        print('''
        1. Train
        2. Fight Trainers in your Local Pokemon Gym
        3. Fight the Elite Four
        4. Display Pokemon Info
        5. Save Game
        6. Load Game
        7. Quit
                ''')
        option = str(input('Please enter "1", "2", "3", "4", "5", "6", or "7".'))
        day += 1
        if option == '1':
            train()
        elif option == '2':
            fight_gym()
        elif option == '3':
            delay_print('The Elite Four are the four strongest pokemon trainers in the world.\n')
            time.sleep(1)
            while True:
                delay_print('Are you sure you want to continue?\n')
                confirmation_battle_elite4 = str(input('Please enter "yes" or "no"'))
                if confirmation_battle_elite4 == 'yes':
                    fight_elite_four()
                    break
                elif confirmation_battle_elite4 == 'no':
                    day -= 1
                    break
                else:
                    print('\nPlease enter "yes" or "no".')
        elif option == '4':
            display_pokemon()
        elif option == '5':
            save_game()
        elif option == '6':
            load_game()
        elif option == '7':
            print('Have a good day!')
            break
        else:
            print('Please enter "1", "2", "3", "4", "5", "6", or "7".')
            day -= 1

#Main
pokemon_game()
