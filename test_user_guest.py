from user_guest import Guest
import unittest
import pytest


class TestGuest(unittest.TestCase):
    test_guest = Guest()

    def test_all_flights(self):
        # Checking that some data is successfully retrieved from the database when the method is called
        self.assertNotEqual(self.test_guest.all_flights(), False)

    def test_display_flight_destination(self):
        # Checking that some data is returned from the method when called with a valid destination
        self.assertNotEqual(self.test_guest.display_flight_destination("LHR"), [])
        # Checking that False is returned when an invalid destination is passed
        self.assertFalse(self.test_guest.display_flight_destination("banana"))

    def test_display_flight_date(self):
        # Checking that some data is returned from the method when called with a datetime object
        self.assertNotEqual(self.test_guest.display_flight_date(dateobject), [])
        # Checking that False is returned when an invalid data type is passed
        self.assertFalse(self.test_guest.display_flight_date("17th of January"))
