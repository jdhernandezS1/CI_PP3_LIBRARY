# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
import datetime
import os


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
            stock = int(books.cell(9, newCol).value)
            condition = stock-rented
            if (condition >= 1):
                val = rented+1
                code = (int(books.cell(10, newCol).value)*2)-1
                x = 1
                client = inventary.cell(x, code).value
                while client is not None:
                    x += 1
                    client = inventary.cell(x, code).value
                y = True
                while y:
                    clear_console()
                    wellcomeMessage()
                    name = input("\n Please type the name of the client: ")
                    if len(name) > 2:
                        y = False
                    else:
                        clear_console()
                        print("The customer's name is short.")
                actualDate = datetime.datetime.now()
                month = str(actualDate.month+2)
                year = str(actualDate.year)
                rentDate = (month + "/" + year)
                clear_console()
                print("The book was Rented as well")
                inventary.update_cell(x, code, name)
                inventary.update_cell(x, code+1, rentDate)
                books.update_cell(8, newCol, str(val))
            else:
                clear_console()
                print("we dont have more copies")
        else:
            clear_console()
            print("we dont have that book")
    except:
        clear_console()
        print("Please be sure than all was written as well")


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
    try:
        cellBook = inventary.find(word)
        cellStock = books.find(word)
        if cellBook is not None:
            row = cellBook.row
            col = cellBook.col
            clear_console()
            wellcomeMessage()
            name = input("\n Please type the Name of the client: ")
            x = 2
            rentClient = (inventary.cell(x, col).value)
            while name != rentClient:
                x += 1
                rentClient = (inventary.cell(x, col).value)
            clientName = inventary.cell(x, col).value
            clientDate = (inventary.cell(x, col+1).value)
            clientDate = clientDate.split("/")
            monthLimit = int(clientDate[0])
            yearLimit = int(clientDate[1])
            actualDate = datetime.datetime.now()
            month = int(actualDate.month)
            year = int(actualDate.year)
            condition1 = (monthLimit >= month and yearLimit >= year)
            condition2 = (yearLimit > year)
            if condition1 or condition2:
                phrase = "The Book was returned on time"
            else:
                if yearLimit < year:
                    month += 12*abs(yearLimit-year)
                tax = (abs(monthLimit-month)*20)
                phrase = "The client is not on time"
                phrase += "the tax of extra time is:" + str(tax) + " $"
            if cellStock is not None:
                stockRow = cellStock.row
                stockCol = cellStock.col
                rented = int(books.cell(8, stockCol).value)
                stock = int(books.cell(9, stockCol).value)
                condition = (stock != stock-rented)
                if (condition):
                    val = rented-1
                    books.update_cell(8, stockCol, str(val))
                    # add 1 value to the stock
                    if x > 1:
                        inventary.update_cell(x, col, "")
                        # deleting the client of the data base
                        inventary.update_cell(x, col+1, "")
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
        cellClient = inventary.findall(client)
        if cellClient != []:
            clear_console()
            print(f"The client {client} has rented:")
            for results in cellClient:
                if results is not None:
                    row = results.row
                    col = results.col
                    clientName = inventary.cell(row, col).value
                    clientDate = inventary.cell(row, col+1).value
                    clientBook = inventary.cell(1, col).value
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
