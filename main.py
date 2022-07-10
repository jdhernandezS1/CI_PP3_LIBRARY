import gspread
import datetime 
#import pandas as pd
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
# Rent book function
# The argument is the sheet where is working
def rentBook(books,inventary):
    word= input("\n Please type the name of the book: ")#the book to search
    cellBook = books.find(word)#cell of the book fint
    if cellBook != None: #verify if we have it 
        row = cellBook.row
        col =cellBook.col
        newCol= col
        newRow = row
        rented = int(books.cell(8, newCol).value)#Rented cell of the book
        stock = int(books.cell(9, newCol).value)#Stock cell of the book
        condition = stock-rented #the condition of the if store have to be more than avaiable or we not have dispnoibility
        if (condition>=1): # if we have books avaiable
            val = rented+1
            code = (int(books.cell(10, newCol).value)*2)-1
            x=1
            client = inventary.cell(x,code).value#initial condition by while 
            while client!= None :   # move in all rows still to empty row
                x+=1
                client = inventary.cell(x,code).value
            name = str(input("\n Please type the name of the client: "))#the client who rent the book
            clientName = inventary.cell(x,code).value #client name
            clientDate = (inventary.cell(x-1,code+1).value) #client Date of rent
            clientDate.split("/") #divide in two the date
            dayRented = clientDate[0]
            monthRented = clientDate[1]
            actualDate = datetime.datetime.now() #actual date
            month = str(actualDate.month+2)
            year = str(actualDate.year)
            rentDate = (month + "/" + year)#new date rented
            # print(rentDate)
            print(clientDate,clientName)
            print("The book was Rented as well")
            inventary.update_cell(x,code, name) # write the name of the client in google sheet
            inventary.update_cell(x,code+1, rentDate)  # write the day of the client must return the book in google sheet
            # books.update_cell(8, newCol, str(val)) # write the book -1 stock 
        else:
            print("we dont have more copies")
    else: 
        print("we dont have that book")
#   Return Book to the library
def returnBook(books):
    word = input("\n Please type the ISBN of the book: ") # the book to search
    cellBook = books.find(word) # cell of the book by isbn
    if cellBook != None: #verify if we have it
        row = cellBook.row  # # of the row where is the book 
        col =cellBook.col    # # of the column where is the book  
        rented = int(books.cell(8, col).value)#Rented cell of the book
        stock = int(books.cell(9, row).value)#Stock cell of the book
        condition = (stock!= stock-rented) #the condition of the if store have to be more than avaiable or we not have dispnoibility
        if (condition) :
            val = rented-1
            books.update_cell(8, newCol, str(val))
            print("The book was returned")
        else:
            print("All the copies of the book are in the store")


        print("The book was Returned")


inventaryValues = inventary.get_all_values()#get values of inventary 
rentBook(books,inventary)