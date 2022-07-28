import gspread
import os
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

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
tst = SHEET.worksheet('test')


def test_login(cred, user, password):
    """
    Validate the credentials
    @param : cred is a reference to an
    object of type worksheet in gspread library
    """
    try:
        userCell = cred.find("user")
        row = userCell.row
        col = userCell.col+1
        usersys = (cred.cell(row, col).value)
        passsys = (cred.cell(row+1, col).value)
        if user == usersys and password == passsys:
            return True
        else:
            print("The User or Password are not in the system")
            return False
    except:
        print("Error please try again")
    input("Press enter to continue")
