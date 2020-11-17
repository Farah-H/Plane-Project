from authentication import Authentication
import unittest
import pytest


class TestAuthentication(unittest.TestCase):
    test_admin_authen = Authentication("jake", "jake", "admin")
    test_user_authen = Authentication("user", "user", "user")
