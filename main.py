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
# Initial declarations
CREDS = Credentials.from_service_account_file('creds.json')#conect with the json file to google sheets
SCOPED_CREDS =  CREDS.with_scopes(SCOPE) 
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Library') # library folder
inventary = SHEET.worksheet('inventary') #inventary sheet
books = SHEET.worksheet('books')# books sheet
fs.clear_console()
print("\n Wellcome to the library")
while True:        
    print("\n Please type an option and press enter:")
    print("\n 1 To rent a book ")
    print("\n 2 To return a book ")
    option = input("\n 3 To get client information  \n\n Option :")
    
    if(option=="1"):
        fs.clear_console()
        fs.rentBook(books,inventary)
    
    elif(option=="2"):
        fs.clear_console()
        fs.returnBook(books,inventary)
    
    elif(option=="3"):
        fs.clear_console()
        fs.findClient(books,inventary)
    
    else:
        print("Please enter a valid option")
