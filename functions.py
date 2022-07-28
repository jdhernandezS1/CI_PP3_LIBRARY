import os
import datetime


def login(cred):
    """
    Validate the credentials
    @param : cred is a reference to an
    object of type worksheet in gspread library
    """
    clear_console()
    wellcomeMessage()
    user = input("\n Please type the username: ")
    # the username
    password = input("\n Please type the password: ")
    # the password
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


def rentBook(books, inventary):
    """
    Rent book function Data base add a new client,
    data and delete one book of the stock
    @param : books is a reference to an object
    of type worksheet in gspread library
    @param : inventary is a reference to an object o
    f type worksheet in gspread library
    """
    flag = True
    while flag:
        wellcomeMessage()
        word = input("\n Please type the name of the book: ")
        # the book to search
        if len(word) > 6:
            flag = False
        else:
            clear_console()
            print("The book name must has min 6 characters")
    try:
        cellBook = books.find(word)
        # cell of the book fint
        if (cellBook is not None):
            # verify if we have it
            row = cellBook.row
            col = cellBook.col
            newCol = col
            newRow = row
            rented = int(books.cell(8, newCol).value)
            # Rented cell of the book
            stock = int(books.cell(9, newCol).value)
            # Stock cell of the book
            condition = stock-rented
            # stock condition
            if (condition >= 1):
                # if we have books avaiable
                val = rented+1
                code = (int(books.cell(10, newCol).value)*2)-1
                x = 1
                client = inventary.cell(x, code).value
                # initial condition by while
                # Find the next empty space
                while client is not None:
                    # move in all rows still to empty row
                    x += 1
                    client = inventary.cell(x, code).value
                y = True
                while y:
                    clear_console()
                    wellcomeMessage()
                    name = input("\n Please type the name of the client: ")
                    # the client who rent the book
                    if len(name) > 2:
                        y = False
                    else:
                        clear_console()
                        print("The customer's name is short.")
                actualDate = datetime.datetime.now()
                # actual date
                month = str(actualDate.month+2)
                year = str(actualDate.year)
                rentDate = (month + "/" + year)
                # new date rented
                clear_console()
                print("The book was Rented as well")
                inventary.update_cell(x, code, name)
                # write the name of the client in google sheet
                inventary.update_cell(x, code+1, rentDate)
                # write the day client must return the book
                books.update_cell(8, newCol, str(val))
                # write the book -1 stock
            else:
                clear_console()
                print("we dont have more copies")
        else:
            clear_console()
            print("we dont have that book")
    except:
        clear_console()
        print("Please be sure than all was written as well")


#   Return Book to the library
def returnBook(books, inventary):
    """
    Rent book function Data base add a new client,
    data and delete one book of the stock
    @param : books is a reference to an object
    of type worksheet in gspread library
    @param : inventary is a reference to an object
    of type worksheet in gspread library
    """
    clear_console()
    wellcomeMessage()
    word = input("\n Please type the book Title: ")
    # the book to search
    try:
        cellBook = inventary.find(word)
        # cell of the book
        cellStock = books.find(word)
        # cell of the book
        if cellBook is not None:
            # verify if we have it
            row = cellBook.row
            # of the row where is the book
            col = cellBook.col
            # of the column where is the book
            clear_console()
            wellcomeMessage()
            name = input("\n Please type the Name of the client: ")
            # the client who rented the book
            x = 2
            rentClient = (inventary.cell(x, col).value)
            # pointer to different clients in the data base
            while name != rentClient:
                x += 1
                rentClient = (inventary.cell(x, col).value)
                # pointer with client located in the data base
            clientName = inventary.cell(x, col).value
            # client name
            clientDate = (inventary.cell(x, col+1).value)
            # client Date of rent
            clientDate = clientDate.split("/")
            # divide in two the date
            monthLimit = int(clientDate[0])
            yearLimit = int(clientDate[1])
            actualDate = datetime.datetime.now()
            # actual date
            month = int(actualDate.month)
            year = int(actualDate.year)
            condition1 = (monthLimit >= month and yearLimit >= year)
            condition2 = (yearLimit > year)
            if condition1 or condition2:
                # condition if the book is on correct date
                phrase = "The Book was returned on time"
            else:
                if yearLimit < year:
                    month += 12*abs(yearLimit-year)
                tax = (abs(monthLimit-month)*20)
                # calculate the tax
                phrase = "The client is not on time"
                phrase += "the tax of extra time is:" + str(tax) + " $"
                # To let know at the staff the tax
            if cellStock is not None:
                # verify if we have it
                stockRow = cellStock.row
                # of the row where is the book
                stockCol = cellStock.col
                # of the column where is the book
                rented = int(books.cell(8, stockCol).value)
                # Rented cell of the book
                stock = int(books.cell(9, stockCol).value)
                # Stock cell of the book
                condition = (stock != stock-rented)
                # the condition of dispnoibility
                if (condition):
                    val = rented-1
                    books.update_cell(8, stockCol, str(val))
                    # add 1 value to the stock
                    if x > 1:
                        # MAKE SURE THAN WE DID DELETE
                        # THE NAME OF BOOKS IN THE STOCK
                        inventary.update_cell(x, col, "")
                        # deleting the client of the data base
                        inventary.update_cell(x, col+1, "")
                        # deleting the client of the data base
                        clear_console()
                        print(phrase)
                    return True
                else:
                    clear_console()
                    print("All the copies of the book are in the store")
                    # The stock is full
                return False
        else:
            clear_console()
            print("Sry but we dont have any book with that name.")
            # is not a book of the library
            return False
    except:
        clear_console()
        print("Please be sure than all was written as well")
        return False


def findClient(books, inventary):
    """
    find client function search a client in the
    data base and show the information to the
    @param : books is a reference to an object
    of type worksheet in gspread library
    @param : inventary is a reference to an object
    of type worksheet in gspread library
    """
    clear_console()
    try:
        wellcomeMessage()
        client = input("\n Please type the Client Name:")
        # the Client to Find
        cellClient = inventary.findall(client)
        # cell of the client
        if cellClient != []:
            clear_console()
            print(f"The client {client} has rented:")
            for results in cellClient:
                # print(results)
                if results is not None:
                    # verify if we have it
                    row = results.row
                    # of the row where is the book
                    col = results.col
                    # of the column where is the book
                    clientName = inventary.cell(row, col).value
                    # client name
                    clientDate = inventary.cell(row, col+1).value
                    # client name
                    clientBook = inventary.cell(1, col).value
                    # client name
                    print(f"Title: {clientBook}")
                    print(f"Maximum Date: {clientDate}")
                    return True
        else:
            print(f"The client {client} is not in the data base.")
            print("Please make you sure the name was typed as well")
            return False
    except:
        return False
        clear_console()
        print("Please be sure than all was written as well")


def wellcomeMessage():
    """
    The function where is the Main Message
    """
    print("\033[1;31;80m ")
    print("                 ░░░░░░░░░░░░░░░░░")
    print("                 ░█░█░███░███░██░░")
    print("                 ░█▀█░█░█░█░█░█░█░")
    print("                 ░▀░▀░▀▀▀░▀▀▀░▀▀░░")
    print("                 ░░░░░░░░░░░░░░░░░")

    print("            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("            ░█░░█░░█▀█░█▀█░█▀█░█▀█░█░█░░")
    print("            ░█░░█░░█▀█░██░░█▀█░██░░░█░░░")
    print("            ░▀▀░▀░░▀▀▀░▀░▀░▀░▀░▀░▀░░▀░░░")
    print("            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("\033[1;33;80m ")


def clear_console():
    """
    Clear the screen
    """
    os.system('clear')


def options():
    """
    The Options on the main menu
    """
    print("\033[1;32;80m")
    print("\n Please type an option and press enter:")
    print("\n 1 To rent a book ")
    print("\n 2 To return a book ")
    print("\n 3 To get client information")
    print("\n 4 To Add book to the stock")
    option = input("\n 5 To log out \n\n Option :")
    return option


def addBook(books, cathegory, tittle, autor, editor, isbn, pages, stock):
    """
    Add book to the database
    """
    rented = 0
    flag = True
    col = 2
    try:
        books.cell(2, 2).value
    except:
        input(" an exeption ocurred")
        return False

    while flag:
        value = books.cell(2, col).value
        if value is None:
            flag = False
        else:
            col += 1

    books.update_cell(2, col, cathegory)
    books.update_cell(3, col, tittle)
    books.update_cell(4, col, autor)
    books.update_cell(5, col, editor)
    books.update_cell(6, col, isbn)
    books.update_cell(7, col, pages)
    books.update_cell(8, col, rented)
    books.update_cell(9, col, stock)
    books.update_cell(10, col, col+1)
    return True
