import gspread
import random
import os
import colorama
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('score')

#print(SHEET.worksheet("score").get_all_values())
color_list = ['Red', 'Green', 'Blue', 'Purple', 'Yellow', 'White','Cyen']
color_list_map = { 'R':'Red', 'G':'Green', 'B':'Blue', 'P':'Purple', 'Y':'Yellow', 'W': 'White', 'C':'Cyen'}
unknown = ['X','X','X','X']
guess_code = ['-','-','-','-']
attempts = 8
input_store={0:['-','-','-','-']}

def clear_screen():
    os.system('clear')

def create_color_code(color_list, choice):
    if choice == 1:
        random_color_code = random.sample(color_list, k=3)
    elif choice == 2:
        random_color_code = random.sample(color_list, k=4)
    elif choice == 3:
        random_color_code = random.sample(color_list, k=5)
    append_unknown_list(choice)
    return random_color_code

def append_unknown_list(k):
    for i in range(2+k):
        unknown.append("X")
        guess_code.append('-')

#def game_board(attempts, unknown, color_passcode):
def game_board(attempts, unknown):
    count = 0
    while attempts > 0:
        welcome = '{:^100}'
        print("*" * 100)
        print()
        print(Fore.RED + welcome.format('GAME BOARD'))
        print(Style.RESET_ALL)
        print("*" * 100)
        print("\n")
        for i in range(len(unknown)):
            unknown[i] = Fore.RED + str(unknown[i]) + Fore.RESET
        print("The secret Color code is: ", end ="")
        print(*unknown, sep=" ")
        print()
        for key in input_store:
            print(" "*10, end="")
            print(f"|  Attempt: {key}", end = "   ")
            l = input_store[key]
            print(*l, sep=" ")
        attempts -= 1
        count += 1
        take_input(count)
        clear_screen()
    print(input_store)
    
    
def take_input(count):
    print("Enter color code: ")
    color_string = input().upper()
    color_code_list = color_string.split()
    color_list =[]
    for color in color_code_list:
        color_list.append(color_list_map[color])    
    #global guess_code 
    #guess_code = color_list
    #print(guess_code)
    input_store[count] = color_list

def compare_colors(passcode, color_input):
    hit = 0
    miss = 0
    for color in color_input:
        if color in passcode:
            if color_input.index(color) == passcode.index(color):
                hit += 1
            else:
                miss += 1
    print(passcode)
    print(color_input)
    print(f'miss:{miss}')
    print(f'hit:{hit}')  
    if hit == 5:
        print(f'Congratulations!!! You won...')
    else:
         print(f'Try again...')

def options_choice():
    print("-" * 20)
    print("Choose difficulty:")
    print("-" * 20)
    print()
    print("1 - ", end="")
    print(Fore.YELLOW + "Easy")
    print(Style.RESET_ALL)
    print("2 - ", end="")
    print(Fore.BLUE + "Medium")
    print(Style.RESET_ALL)
    print("3 - ", end="")
    print(Fore.RED + "Difficult")
    print(Style.RESET_ALL)

    print("Enter your choice by pressing '1', '2' or '3' : ")
    while True:
        key = input()
        if key in ['1','2','3']:
            break
        else:
            print("Invalid input, choose again!")
    return int(key)


def main():
    clear_screen()
    choice = options_choice()
    color_passcode = create_color_code(color_list, choice)
    game_board(attempts, unknown, color_passcode)
    color_input = take_input()
    compare_colors(color_passcode, color_input)

def welcome():
    welcome = '{:^100}'
    print("*" * 100)
    print()
    print(Fore.RED + welcome.format('BREAK THE COLOR CODE'))
    print(Style.RESET_ALL)
    print("*" * 100)

    print("""
You have to crack the color code in as few attempts
as possible. There are total of 8 attempts.

The color code will be consisting of either 3, 4, or 5 colors , depending on the difficulty 
of the game you choose (Easy, Medium or Difficult).

Example:
Easy : Green White Yellow
Medium: White Yellow Red Blue
Difficult: Green White Red Purple Blue

You will be asked to enter your color code guess.  

You will be told how close you are if you don't get the exact code

Hit -> If you get a right color on exact position
Miss-> If you get the right color but on different position

If you get the color code exactly right you have won the game.

GOOD LUCK !!! """)

    print("Press 'C' or 'c' to continue.../n")
    while True:
        key = input()
        if(key.upper() == 'C'):
            main()
            break
        else:
            print("Invalid input, Try again!")
            continue
#welcome()
game_board(attempts, unknown)




