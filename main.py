
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')#conect with the json file to google sheets
SCOPED_CREDS =  CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
#open the document Library
SHEET = GSPREAD_CLIENT.open('Library') 
#open the internal sheet inventary
inventary = SHEET.worksheet('inventary')
#open the internal sheet books
books = SHEET.worksheet('books')
#open the internal sheet test
# test = SHEET.worksheet('test')
inventaryValues = inventary.get_all_values()
cellBook = books.find("Atomic Habits")
row = cellBook.row
col =cellBook.col
newCol= col
newRow = row+6
rented = int(books.cell(8, newCol).value)
store = int(books.cell(9, newCol).value)
condition = store-rented #the condition of the if store have to be more than avaiable or we not have dispnoibility
if (condition>=1):
    val = rented+1
    books.update_cell(8, newCol, str(val))
else:
    print("we dont have more copies")

