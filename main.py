
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# Initial declarations
CREDS = Credentials.from_service_account_file('creds.json')#conect with the json file to google sheets
SCOPED_CREDS =  CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Library') 
inventary = SHEET.worksheet('inventary')
books = SHEET.worksheet('books')
#Rent book function
# The argument is the sheet where is working
def rentBook(books):
    word= input("\n Please type the name of the book: ")#the book to search
    cellBook = books.find(word)#cell of the book fint
    if cellBook != None: #verify if we have it 
        row = cellBook.row
        col =cellBook.col
        newCol= col
        newRow = row+6
        rented = int(books.cell(8, newCol).value)#Rented cell of the book
        stock = int(books.cell(9, newCol).value)#Stock cell of the book
        condition = stock-rented #the condition of the if store have to be more than avaiable or we not have dispnoibility
        if (condition>=1):
            val = rented+1
            books.update_cell(8, newCol, str(val))
            print("The book was returned")
        else:
            print("we dont have more copies")
    else: 
        print("we dont have that book")

def returnBook(books):
    word = input("\n Please type the ISBN of the book: ") # the book to search
    cellBook = books.find(word) # cell of the book by isbn
    print("The book was Returned")


inventaryValues = inventary.get_all_values()#get values of inventary 
rentBook(books)