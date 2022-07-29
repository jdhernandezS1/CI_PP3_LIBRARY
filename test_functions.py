# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
import unittest
import functions as fs
import validation as val


class TestAdd(unittest.TestCase):
    """
    Verification add book function
    is working
    """
    def test_add_book_True(self):
        self.assertTrue(fs.addBook(val.tst, "c", "t", "a", "e", "i", "p", "s"))

    def test_add_book_False(self):
        self.assertFalse(fs.addBook("sopa", "c", "t", "a", "e", "i", "p", "s"))


class TestCred(unittest.TestCase):
    """
    Verification Credentials
    are working
    """
    def test_validate_credentials_True(self):
        self.assertTrue(val.test_login(val.cred, "admin", "admin"))

    def test_validate_credentials_False(self):
        self.assertFalse(val.test_login(val.cred, "test", "test"))


class TestFuncs(unittest.TestCase):
    """
    Verification Functions
    are working
    """
    def test_rent_book(self):
        self.assertFalse(fs.rentBook(val.books, val.inventary))

    def test_return_book(self):
        self.assertFalse(fs.returnBook(val.books, val.inventary))

    def test_find_client(self):
        self.assertFalse(fs.findClient(val.books, val.inventary))
