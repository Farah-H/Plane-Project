from authentication import Authentication
import unittest
import pytest


class TestAuthentication(unittest.TestCase):
    test_authen = Authentication("jake", "jake")

    def test_credential_manager(self):
        # Checking the result when a  user is found in the database
        self.assertNotEqual(self.test_authen.credential_manager("jake"), False)
        # Checking the result when a user is not found
        self.assertFalse(self.test_authen.credential_manager("barrybluejeans"))

    def test_check_login(self):
        # Checking the result when the login credentials are correct for an admin
        self.assertEqual(self.test_authen.check_login("jake", "jake"), "admin")
        # Checking the result when the login credentials are correct for a user
        self.assertEqual(self.test_authen.check_login("user", "user"), "user")
        # Checking the result when the login credentials are incorrect
        self.assertFalse(self.test_authen.check_login("jake", "notjake"))

    def test_db_credentials(self):
        # Checking if an exception is raised when the user can't log in with the provided details
        self.assertRaises(Exception, self.test_authen.db_credentials(False))
        # Checking if
        checking_admin_tuple = ("jake", "admin")
        self.assertTupleEqual(checking_admin_tuple, self.test_authen.db_credentials("admin"))
        checking_user_tuple = ("user", "user")
        self.assertTupleEqual(checking_user_tuple, self.test_authen.db_credentials("user"))

    def test_password(self):
        pass

    def test_hashpass(self):
        pass

    def test_checkhash(self):
        pass

