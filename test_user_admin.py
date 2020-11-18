from user_admin import Admin
import unittest
import pytest


class TestAdmin(unittest.TestCase):
    test_admin = Admin()

    def test_add_staff(self):
        pass

    def test_remove_staff(self):
        pass

    def test_change_permissions(self):
        pass

    def test_view_user(self):
        # Checking that the method returns the expected information for a user in the database
        expected_list = ["Mr.", "Jeff", "Bridges", "64 Zoo Lane", "05/11/1958"]
        self.assertListEqual(expected_list, self.test_admin.view_user("jeff"))
        # Checking the output when the method is called with a username not found in the database
        self.assertFalse(self.test_admin.view_user("barrybluejeans"))

    def test_edit_flight(self):
        # Checking the method returns correct output when passed a valid flight number and a new flight destination
        new_locations_dict = {"flight_destination": "Lisbon", "departure_location": "London"}
        self.assertTrue(self.test_admin.edit_flight("SA 74", new_locations_dict))
        # Checking if the method returns the correct output when passed a non-existent flight number
        self.assertFalse(self.test_admin.edit_flight("NO 00", new_locations_dict))
        # Checking if the method returns the correct output when passed a non dictionary
        new_locations_list = ["Lisbon", "London"]
        self.assertFalse(self.test_admin.edit_flight("NO 00", new_locations_list))
        # Checking if the method returns the correct output when passed a dictionary with invalid keys
        bad_keys_dict = {"I_want_to_go_here": "Lisbon", "From_here_please": "London"}
        self.assertFalse(self.test_admin.edit_flight("NO 00", bad_keys_dict))

    def test_add_flight(self):
        pass
