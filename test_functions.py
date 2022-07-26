import unittest
import functions as fs
import validation as val


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
        self.assertNotIsInstance(fs.rentBook(val.books, val.inventary))

    def test_return_book(self):
        self.assertNotIsInstance(fs.returnBook(val.books, val.inventary))

    def test_find_client(self):
        self.assertNotIsInstance(fs.findClient(val.books, val.inventary))


class Test_wellcomeMessage(unittest.TestCase):
    """
    Verification wellcome
    message
    """
    def test_message(self):
        self.assertNotIsInstance(fs.wellcomeMessage())
