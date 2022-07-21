# import PySimpleGUI as sg
import gspread
import os
import functions as fs
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
try:
    # Initial declarations
    CREDS = Credentials.from_service_account_file('creds.json')
    #  conect with the json file to google sheets
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('Library')
    # library folder
    inventary = SHEET.worksheet('inventary')
    # inventary sheet
    books = SHEET.worksheet('books')
    # books sheet
    cred = SHEET.worksheet('cred')
    # credentials sheet
except:
    ("an error ocurred")
    quit()

while True:
    flag = False
    fs.clear_console()
    print("\033[1;32;80m")

    try:
        flag = fs.login(cred)
    except:
        print("exeption please try Reload the page")
    while flag:
        fs.clear_console()
        fs.wellcomeMessage()
        option = fs.options()
        if(option == "1"):
            fs.clear_console()
            fs.rentBook(books, inventary)
        elif(option == "2"):
            fs.clear_console()
            fs.returnBook(books, inventary)
        elif(option == "3"):
            fs.clear_console()
            fs.findClient(books, inventary)
        elif(option == "4"):
            print("Please Press Reload button to start again")
            fs.clear_console()
            flag = False
        else:
            print("Please enter a valid option")
        input("Press enter to continue")
