import gspread
import random
from google.oauth2.service_account import Credentials

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
color_list = ['Red', 'Green', 'Blue', 'Purple', 'Yellow', 'White']
color_list_map = { 'R':'Red', 'G':'Green', 'B':'Blue', 'P':'Purple', 'Y':'Yellow', 'W': 'White'}


def create_color_code(color_list):
    random_color_code = random.sample(color_list, k=5)
    return random_color_code

def take_input():
    print("Enter color code: ")
    color_string = input().upper()
    color_code_list = color_string.split()
    color_list =[]
    for color in color_code_list:
        color_list.append(color_list_map[color])    
    return color_list
    #print(f'You enter {color_code} : {color_list_map[color_code]}')

color_passcode = create_color_code(color_list)
color_input = take_input()

def compare_colors(passcode, color_input):
    hit = 0
    miss = 0
    flag = 0
    
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

compare_colors(color_passcode, color_input)
