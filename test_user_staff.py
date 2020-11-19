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
        self.assertFalse(self.test_staff.change_passenger("Barry Blue Jeans", "journey_id", 9))

    def test_display_flight(self):
        # Format of list is [terminal_id, departure_time, arrival_time, airport_code(dep_from), airport_code(arrive_at)]
        expected_list = [1, "2020-08-02 13:00:00", "2020-08-02 18:00:00", "LHR", "GDG"]
        # Checking if the correct data is retrieved from the database when the method is called
        self.assertListEqual(self.test_staff.display_flight(8), expected_list)

    def test_display_passenger(self):
        # Checking if passenger data is returned for a passenger that exists in the database
        self.assertNotEqual(self.test_staff.display_passenger("Jeff", "Bridges"), False)
        # Checking if nothing is returned for a passenger that doesn't exist in the database
        self.assertFalse(self.test_staff.display_passenger("Barry", "Blue Jeans"))
