import gspread
import random
import os
import sys
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
unknown = []
guess_code = []
attempts = 8
input_store={0:guess_code}
clue = {0:[0,0]}

def reset_variables():
    global unknown
    unknown = []
    global  guess_code 
    guess_code = []
    global input_store 
    input_store={0:guess_code}
    global clue
    clue = {0:[0,0]}


def clear_screen():
    os.system('clear')

def continue_to_main():
    print("Press 'C' or 'c' to continue...")
    while True:
        key = input()
        if(key.upper() == 'C'):
            main()
            break
        else:
            print("Invalid input, Try again!")
            continue
def welcome_banner():
    welcome = '{:^100}'
    print("*" * 100)
    print()
    print(Fore.RED + welcome.format('BREAK THE COLOR CODE'))
    print(Style.RESET_ALL)
    print("*" * 100)

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
        unknown.append("***")
        guess_code.append('---')


def game_board(unknown):
    welcome_banner()
    welcome1 = '{:^100}'
    print("*" * 100)
    print()
    print(Fore.RED + welcome1.format('GAME BOARD'))
    print(Style.RESET_ALL)
    print("*" * 100)
    print("\n")
    for i in range(len(unknown)):
        unknown[i] = Fore.RED + str(unknown[i]) + Fore.RESET
    print("The secret Color code is: ", end ="")
    print(*unknown, sep=" ")
    print()


def guess_attempts(attempts, unknown, color_passcode, choice):
    count = 0
    flag = 0
    print(color_passcode)
    while True:
        game_board(unknown)
        for key in input_store:
            print(" "*10, end="")
            print(f"|  Attempt: {key}", end = "   ")
            print(f'Hits: {clue[key][0]},  Misses: {clue[key][1]}', end="    ")
            dict_list = input_store[key]
            print(*dict_list, sep=" ")
            if check_result(count, attempts,key, choice):
                pass
        count += 1
        color_input = take_input(count, choice)
        compare_colors(color_passcode, color_input,count)  
        clear_screen()
    
        
def check_result(count, attempt , key, choice):
    if count == attempt:
        clear_screen()
        print(Fore.BLUE + f"You ran out of attempts! Better luck next time...\n\n" + Fore.RESET)
        continue_to_main()    

    if clue[key][0] == choice+2:
        clear_screen()
        print(Fore.GREEN + f"CONGRATULATIONS! You broke the code in {count} attempts, Nice work!!!\n\n" + Fore.RESET)
        continue_to_main()

    return False

    
def take_input(count, choice):
    length = choice + 2
    print(f"\nEnter code consisting of {length} colors.")
    print(f"Example -> r/R for Red, b/B for Blue and so on.")
    print(f"Color choices: ['Red', 'Green', 'Blue', 'Purple', 'Yellow', 'White','Cyen']")
    print(f"If you want to go to the main menu. Type 'menu'.")
    print(f"If you want to exit the game. Type 'exit'.\n")
    while True:
        color_string = input().upper()
        color_code_list = color_string.split()

        if validate_input(color_code_list,length):
            break
    color_input =[]
    for color in color_code_list:
        color_input.append(color_list_map[color])    
    input_store[count] = color_input
    return color_input


def validate_input(color_code_list,length):
    flag = 0
    if color_code_list == ['MENU']:
        continue_to_main()
        
    if color_code_list == ['EXIT']:
        sys.exit(0)
    try:
        if len(color_code_list) != length:
            raise ValueError( f"Exactly {length} values required, you provided {len(color_code_list)}")
    except ValueError as e:
        print(f"Invalid input: \n{e}! Type again...\n")
        return False
    
    for color in color_code_list:
        if color not in ['R','G','B','P','Y','W','C']:
                flag = 1
    if flag == 1:
            print(f"Invalid input: \nChoose as described in istructions! Type again...")
            return False
    return True
    

def compare_colors(passcode, color_input, count):
    hit = 0
    miss = 0
    
    for color in color_input:
        if color in passcode:
            if color_input.index(color) == passcode.index(color):
                hit += 1
            else:
                miss += 1
    l = [hit, miss]
    clue[count] = l
  
    


def options_choice():
    welcome_banner()
    print("-" * 20)
    print("Choose difficulty:")
    print("-" * 20)
    print()
    print("1 - ", end="")
    print(Fore.YELLOW + "Easy" + Fore.RESET)
    print("2 - ", end="")
    print(Fore.BLUE + "Medium" + Fore.RESET)
    print("3 - ", end="")
    print(Fore.RED + "Difficult" + Fore.RESET)
    print("4 - ", end="")
    print(Fore.GREEN + "Exit Game" + Fore.RESET)

    print("Enter your choice by pressing '1', '2', '3 or '4'")
    while True:
        key = input()
        if key in ['1','2','3','4']:
            break
        else:
            print("Invalid input, choose again!")
    if (int(key) == 4):
        sys.exit(0)
    clear_screen()
    return int(key)


def main():
    clear_screen()
    reset_variables()
    choice = options_choice()
    color_passcode = create_color_code(color_list, choice)
    guess_attempts(attempts, unknown, color_passcode, choice)
    

def welcome():
    welcome_banner()
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
    continue_to_main()


welcome()







