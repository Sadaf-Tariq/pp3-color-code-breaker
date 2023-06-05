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
color_list = ['Red', 'Green', 'Blue', 'Purple' 'Yellow', 'White']
color_list_map = { 'R':'Red', 'G':'Green', 'B':'Black', 'P':'Purple', 'Y':'Yellow', 'W': 'White'}


def create_color_code(color_list):
    random_color_code = random.sample(color_list, k=3)
    return random_color_code

print(create_color_code(color_list))
print("Enter color code: ")
color_code = input().upper()
print(f'You enter {color_code} : {color_list_map[color_code]}')