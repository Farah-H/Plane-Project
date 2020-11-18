from user_guest import Guest
import unittest
import pytest


class TestGuest(unittest.TestCase):
    test_guest = Guest()

    def test_all_flights(self):


    def test_display_flight(self):
        # Checking that some data is returned from the method when called with a valid flight reference
        self.assertIsNotNone(self.test_guest.display_flight(8))
        # Checking that False is returned when an invalid flight reference is passed
        self.assertFalse(self.test_guest.display_flight("banana"))
