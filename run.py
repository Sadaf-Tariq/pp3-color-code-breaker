import gspread
import random
from os import system
import sys
import time
from google.oauth2.service_account import Credentials
from colorama import Fore
from operator import itemgetter

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('score')


color_list = ['Red', 'Green', 'Blue', 'Purple', 'Yellow', 'White', 'Cyan']
color_list_map = {'R': 'Red', 'G': 'Green', 'B': 'Blue', 'P': 'Purple',
                  'Y': 'Yellow', 'W': 'White', 'C': 'Cyan'}
unknown = []
guess_code = []
attempts = 8
input_store = {0: guess_code}
clue = {0: [0, 0]}
player_name = ''
score = 0


class Score:
    """
    Class to store score details in spreadsheet
    """
    def __init__(self, name, score, level):
        self.name = name
        self.score = score
        self.level = level

    def update(self):
        level_str = ''
        if self.level == 1:
            level_str = 'easy'
        elif self.level == 2:
            level_str = 'medium'
        elif self.level == 3:
            level_str = 'difficult'
        data = [self.name, self.score, level_str]
        score_sheet = SHEET.worksheet('score')
        score_sheet.append_row(data)


def reset_variables():
    """
    Resets global variables when user wants to play again,
    aim is to not repeat or store incorrect values in spreadsheet
    """
    global unknown
    unknown = []
    global guess_code
    guess_code = []
    global input_store
    input_store = {0: guess_code}
    global clue
    clue = {0: [0, 0]}


def clear_screen():
    """
    Cleans sccreen
    """
    system('clear')


def continue_to_main():
    """
    This function takes back to main menu
    """
    print("Press 'C' or 'c' to continue...")
    while True:
        key = input('\n')
        if (key.upper() == 'C'):
            main()
            break
        else:
            print("Invalid input, Try again!")
            continue


def welcome_banner():
    """
    Prints welcome heading on top of the screen
    """
    welcome = '{:^80}'
    print("*" * 80)
    print()
    print(Fore.RED + welcome.format("MASTERMIND - CODE BREAKER")
          + Fore.RESET + '\n')
    print("*" * 80)


def player_namef():
    """
    Takes username input
    """
    name = '{:^80}'
    print('\n\n\n')
    print(Fore.RED + name.format('Enter your first name:') + Fore.RESET)
    print(' '*37, end="")
    global player_name
    while True:
        try:
            player_name = input()
            if not player_name.isalpha():
                raise ValueError(f"Enter a valid name.")
            else:
                break
        except ValueError as e:
            print(f"Invalid input: {e}!")
    return True


def create_color_code(color_list, choice):
    """
    Creates the color code for user to guess
    """
    if choice == 1:
        random_color_code = random.sample(color_list, k=3)
    elif choice == 2:
        random_color_code = random.sample(color_list, k=4)
    elif choice == 3:
        random_color_code = random.sample(color_list, k=5)
    append_unknown_list(choice)
    return random_color_code


def append_unknown_list(k):
    """
    Appends '***' and '---' for the game board
    acocording to the user choice
    """
    for i in range(2+k):
        unknown.append("***")
        guess_code.append('---')


def game_board(unknown):
    """
    Prints game board for the play
    """
    welcome1 = '{:^80}'
    print("*" * 80)
    print()
    print(Fore.RED + welcome1.format('GAME BOARD') + Fore.RESET + '\n')
    print("*" * 80)
    print("\n")
    for i in range(len(unknown)):
        unknown[i] = Fore.RED + str(unknown[i]) + Fore.RESET
    print("The secret Color code is: ", end="")
    print(*unknown, sep=" ")
    print()


def add_rank(j, rank, color):
    """
    Add ranks to the updated scoreboard
    """
    print(color + ' '*22, end="")
    print(f"{j[0]+rank:16}", end="")
    print(f"{j[1]:<17}", end="")
    print(f"{j[2]}")


def leaderboard():
    """
    Prints scoreboard(top 10) after a games is finished
    """
    clear_screen()
    game_board = '{:^80}'
    print("*" * 80)
    print()
    print(Fore.RED + game_board.format('SCOREBOARD') + Fore.RESET + '\n')
    print("*" * 80)
    print('\n')
    score_sheet = SHEET.worksheet('score').get_all_values()
    score_sheet_headings = score_sheet[0]
    score_values = score_sheet[1:]
    for i in score_values:
        i[1] = int(i[1])
    new_ssh = '            '.join(score_sheet_headings).upper()
    underlined_text = "\x1B[4m" + new_ssh + "\x1B[0m"
    print(Fore.RED + underlined_text.center(90, ' ') + Fore.RESET + '\n')
    sorted_list = sorted(score_values, key=itemgetter(1), reverse=True)
    for j in sorted_list[0:10]:
        if sorted_list.index(j) == 0:
            add_rank(j, '(1)', Fore.YELLOW)
        elif sorted_list.index(j) == 1:
            add_rank(j, '(2)', Fore.BLUE)
        elif sorted_list.index(j) == 2:
            add_rank(j, '(3)', Fore.GREEN)
        else:
            add_rank(j, '', Fore.RESET)
    continue_to_main()


def guess_attempts(attempts, unknown, color_passcode, choice):
    """
    Prints attempts detail on the screen after each attempt
    made by the user
    """
    count = 0
    flag = 0
    while True:
        game_board(unknown)
        for key in input_store:
            print(" "*10, end="")
            print(f"|  Attempt: {key}", end="   ")
            print(f'Hits: {clue[key][0]},  Misses: {clue[key][1]}', end="    ")
            dict_list = input_store[key]
            print(*dict_list, sep=" ")
            if check_result(count, attempts, key, choice, color_passcode):
                pass
        count += 1
        if count == attempts+1:
            time.sleep(2.5)
            check_result(count, attempts, key, choice, color_passcode)
        color_input = take_input(count, choice)
        compare_colors(color_passcode, color_input, count)
        clear_screen()


def check_result_if(print_string, flag, count, attempt, key,
                    choice, color_passcode):
    time.sleep(2.5)
    clear_screen()
    game_board(color_passcode)
    print(Fore.BLUE + print_string)
    cal_score(count, flag)
    print(Fore.RESET)
    score_obj = Score(player_name, score, choice)
    score_obj.update()
    continue_to_main()


def check_result(count, attempt, key, choice, color_passcode):
    """
    Checks result when user enters a guess,
    this function compares the user guess with
    the random code generated
    """
    if count == attempt+1:
        print_string = f"You ran out of attempts! Better luck next time...\n\n"
        check_result_if(print_string, 1, count, attempt, key,
                        choice, color_passcode)

    if clue[key][0] == choice+2:
        print_string = f"CONGRATULATIONS! You broke the code in {count}\
 attempt(s), Nice work!!!\n\n"
        check_result_if(print_string, 0, count, attempt, key, choice,
                        color_passcode)

    return False


def cal_score(count, flag):
    """
    This function calculates the store based on the count of attempts
    a code is caracked or could not be cracked under 8 attempts
    """
    global score
    if flag == 1:
        score = 0
        print(f"Your score: {score} ")
        return score
    else:
        score = (10-(count-1))*10
        print(f"Your score: {score} ")


def take_input(count, choice):
    """
    Takes input (code guess) from the user
    """
    length = choice + 2
    print(f"\nEnter code consisting of {length} colors.")
    print(f"Example -> r/R for Red, b/B for Blue with whitespace.\
    Don't repeat colors.")
    print(f"Color choices: ['Red', 'Green', 'Blue', 'Purple',\
    'Yellow', 'White','Cyen']")
    print(f"For main menu -> type 'menu', to exit -> type 'exit'\n")
    while True:
        color_string = input('\n').upper()
        color_code_list = color_string.split()

        if validate_input(color_code_list, length):
            break
    color_input = []
    for color in color_code_list:
        color_input.append(color_list_map[color])
    input_store[count] = color_input
    return color_input


def validate_input(color_code_list, length):
    """
    Validates the color code input against duplicate values,
    non string values, more or less color codes then required
    """
    flag_1 = 0
    flag_2 = 0
    if color_code_list == ['MENU']:
        continue_to_main()

    if color_code_list == ['EXIT']:
        sys.exit(0)
    try:
        if len(color_code_list) != length:
            raise ValueError(f"Exactly {length} values required,\
 you provided {len(color_code_list)}")
    except ValueError as e:
        print(f"Invalid input: \n{e}! Type again...\n")
        return False
    for color in color_code_list:
        if color not in ['R', 'G', 'B', 'P', 'Y', 'W', 'C']:
            flag_1 = 1
    if flag_1 == 1:
        print(f"Invalid input: \nChoose as described in istructions!\
 Type again...\n")
        return False

    for color in color_code_list:
        num = color_code_list.count(color)
        if num > 1:
            flag_2 = 1
    if flag_2 == 1:
        print(f"Invalid input: \nDo not repeat colors! Type again...\n")
        return False
    return True


def compare_colors(passcode, color_input, count):
    """
    Compares the actual color code with user's guess to
    give clue to the user
    """
    hit = 0
    miss = 0

    for color in color_input:
        if color in passcode:
            if color_input.index(color) == passcode.index(color):
                hit += 1
            else:
                miss += 1
    list_new = [hit, miss]
    clue[count] = list_new


def options_choice():
    """
    Gives game level options to the user to choose
    """
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
    print(Fore.MAGENTA + "Scoreboard" + Fore.RESET)
    print("5 - ", end="")
    print(Fore.GREEN + "Exit Game" + Fore.RESET)

    print("Enter your choice by pressing '1', '2', '3' ,'4' or '5':")
    while True:
        key = input('\n')
        if key in ['1', '2', '3', '4', '5']:
            break
        else:
            print("Invalid input, choose again!")
    if (int(key) == 4):
        leaderboard()
        return 0
    if (int(key) == 5):
        sys.exit(0)
    clear_screen()
    return int(key)


def main():
    """
    Main function to start the game
    """
    clear_screen()
    reset_variables()
    choice = options_choice()
    color_passcode = create_color_code(color_list, choice)
    guess_attempts(attempts, unknown, color_passcode, choice)


def welcome():
    """
    Welcome function to display welcome heading and instruction
    """
    welcome_banner()

    if player_namef():
        clear_screen()
        welcome_banner()
        print("\n")
        pname = '{:^80}'
        print("*" * 80)
        print()
        print(Fore.RED + pname.format('welcome  ' + player_name + '!!!')
              + Fore.RESET)
        print()
        print("*" * 80)
        print()
        while True:
            print("Press 'I' or 'i' for Instructions.")
            print("Press 'M' or 'm' for Game menu.")
            rkey = input('\n')
            if rkey.upper() == 'I':
                clear_screen()
                print("""
You have to crack the color code in as few attempts
as possible. There are total of 8 attempts.
The color code will be consisting of either 3, 4, or\
5 colors , depending on the difficulty
of the game you choose (Easy, Medium or Difficult).

Easy : Green White Yellow
Medium: White Yellow Red Blue
Difficult: Green White Red Purple Blue

You will be asked to enter your color code guess.
You will be told how close you are if you don't get the exact code

Hit -> If you get a right color on exact position
Miss-> If you get the right color but on different position

If you get the color code exactly right you have won the game.
GOOD LUCK !!! """)
                print()
                break
            elif rkey.upper() == 'M':
                main()
            else:
                print("Invalid input! Try again")
        continue_to_main()


welcome()
