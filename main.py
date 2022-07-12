# import PySimpleGUI as sg
import gspread
import datetime
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
            #Find the next empty space  
            while client!= None :   # move in all rows still to empty row
                x+=1
                client = inventary.cell(x,code).value
            name = str(input("\n Please type the name of the client: "))#the client who rent the book
            actualDate = datetime.datetime.now() #actual date
            month = str(actualDate.month+2)
            year = str(actualDate.year)
            rentDate = (month + "/" + year)#new date rented
            # print(clientDate,clientName)
            print("The book was Rented as well")
            inventary.update_cell(x,code, name) # write the name of the client in google sheet
            inventary.update_cell(x,code+1, rentDate)  # write the day of the client must return the book in google sheet
            books.update_cell(8, newCol, str(val)) # write the book -1 stock 
        else:
            print("we dont have more copies")
    else: 
        print("we dont have that book")
#   Return Book to the library
def returnBook(books,inventary):
    word = input("\n Please type the book Title: ") # the book to search
    cellBook = inventary.find(word) # cell of the book 
    cellStock = books.find(word) # cell of the book 
    if cellBook != None: #verify if we have it
        row = cellBook.row  # # of the row where is the book 
        col =cellBook.col    # # of the column where is the book  
        name = input("\n Please type the Name of the client: ") # the client who rented the book
        x=2
        rentClient = (inventary.cell(x, col).value)#pointer to different clients in the data base   
        while name!=rentClient:
            x+=1
            rentClient = (inventary.cell(x, col).value)#pointer with client located in the data base   
        
        clientName = inventary.cell(x,col).value #client name
        clientDate = (inventary.cell(x,col+1).value) #client Date of rent
        clientDate = clientDate.split("/") #divide in two the date
        monthLimit = int(clientDate[0])
        yearLimit = int(clientDate[1])
        actualDate = datetime.datetime.now() #actual date
        month = int(actualDate.month)
        year = int(actualDate.year)
        if (monthLimit >= month and yearLimit >= year)or (yearLimit > year) :# condition if the book is on correct date
            phrase= "The Book was returned on time"
        else :
            if yearLimit < year:
                month+=12*abs(yearLimit-year)
            tax= (abs(monthLimit-month)*20) #calculate the tax
            phrase= "The client is not in time the tax of extra time is:"+ str(tax) + " $" # To let know at the staff the tax
        if cellStock!=None: #verify if we have it
            stockRow = cellStock.row  # # of the row where is the book 
            stockCol = cellStock.col    # # of the column where is the book 
            rented = int(books.cell(8, stockCol).value)#Rented cell of the book
            stock = int(books.cell(9, stockCol).value)#Stock cell of the book
            condition = (stock!= stock-rented) #the condition of the if store have to be more than avaiable or we not have dispnoibility        
            if (condition) :
                val = rented-1
                books.update_cell(8, stockCol, str(val))#add 1 value to the stock 
                if x>1: #MAKE SURE THAN WE DONT DELETE THE NAME OF BOOKS IN THE STOCK
                    inventary.update_cell(x,col,"")#deleting the client of the data base
                    inventary.update_cell(x,col+1,"")#deleting the client of the data base
                    print(phrase)
            else:
                print("All the copies of the book are in the store") #The stock is full 
    else:
        print("Sry but we dont have any book with that name.") # is not a book of the library
# fin client function 
def findClient(books,inventary):
    client = input("\n Please type the Client Name:") # the Client to Find
    cellClient = inventary.findall(client) # cell of the client 
    if cellClient!=[]:
        print(f"The client {client} has rented:")
        for results in cellClient:
            # print(results)
            if results != None: #verify if we have it
                row = results.row  # # of the row where is the book 
                col =results.col    # # of the column where is the book  
                clientName = inventary.cell(row,col).value #client name
                clientDate = inventary.cell(row,col+1).value #client name
                clientBook = inventary.cell(1,col).value #client name
                print(f"Title: {clientBook}")
                print(f"Maximum Date: {clientDate}")
    else:
        print(f"The client {client} is not in the data base.\n Please make you sure the name was typed as well")

# inventaryValues = inventary.get_all_values()#get values of inventary 
# rentBook(books,inventary)
# returnBook(books,inventary)
# findClient(books,inventary)