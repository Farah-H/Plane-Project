from authentication import Authentication
import unittest
import pytest


class TestAuthentication(unittest.TestCase):
    test_admin_authen = Authentication("jake", "jake", "admin")
    test_user_authen = Authentication("user", "user", "user")

    def test_credential_manager(self):
        # Checking the result when a  user is found in the database
        self.assertNotEqual(self.test_user_authen.credential_manager("jake"), False)
        # Checking the result when a user is not found
        self.assertFalse(self.test_user_authen.credential_manager("barrybluejeans"))

    def test_check_login(self):
        self.assertTrue(self.test_admin_authen.check_login("jake", "jake"))
        self.assertFalse(self.test_admin_authen.check_login("jake", "notjake"))

    def test_db_credentials(self):
        pass

    def test_password(self):
        pass

    def test_hashpass(self):
        pass

    def test_checkhash(self):
        pass

