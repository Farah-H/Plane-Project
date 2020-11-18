from user_staff import Staff
import unittest
import pytest


class TestStaff(unittest.TestCase):
    test_staff = Staff()

    def test_add_passenger(self):
        # Checking if it adds a passenger with their full name, passport number and journey ID
        self.assertTrue(self.test_staff.add_passenger("Jeff Bridges", "109841757", 8))
        # Checking if it adds a passenger with their full name but an invalid passport number and journey ID
        self.assertFalse(self.test_staff.add_passenger("Jeff Bridges", "thisisnotright", "8"))

    def test_change_passenger(self):
        # Checking if the method successfully changes a passenger's details if put on the wrong flight
        self.assertTrue(self.test_staff.change_passenger("Jeff Bridges", "journey_id", 9))
        # Checking if the method successfully changes a passenger's details if the passenger does not exist
        self.assertTrue(self.test_staff.change_passenger("Barry Blue Jeans", "journey_id", 9))

    def test_display_flight(self):
        pass

    def test_get_data(self):
        # Checking if data can be successfully queried from the database
        self.assertIsNotNone(self.test_staff.get_data("journey_details"))
        # Checking the output when the table is empty or does not exist
        self.assertFalse(self.test_staff.get_data("journey_detailz"))

    def test_display_passenger(self):
        # Checking if passenger data is returned for a passenger that exists in the database
        self.assertIsNotNone(self.test_staff.display_passenger("Jeff", "Bridges"))
        # Checking if nothing is returned for a passenger that doesn't exist in the database
        self.assertIsNone(self.test_staff.display_passenger("Barry", "Blue Jeans"))

    def test_check_seats(self):
        # Checking if the correct seat number is returned when given a flight reference(journeyid) and passenger id
        self.assertEqual(self.test_staff.check_seats(8, 1), 54)
        # Checking what is output when looking for a seat number of a passenger that isn't on that flight
        self.assertFalse(self.test_staff.check_seats(8, 18))
