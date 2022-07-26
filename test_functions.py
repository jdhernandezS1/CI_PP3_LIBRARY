import unittest
import functions as fs
import validation as val


class TestCred(unittest.TestCase):
    """
    Verification Credentials
    are working
    """
    def test_validate_credentials_True(self):
        self.assertTrue(val.test_login(val.cred,"admin","admin"))

    def test_validate_credentials_False(self):
        self.assertFalse(val.test_login(val.cred,"test","test"))
