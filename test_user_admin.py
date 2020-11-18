from user_admin import Admin
import unittest
import pytest


class TestAdmin(unittest.TestCase):
    test_admin = Admin()

    def test_add_staff(self):
        # Checking the result when trying to add someone new
        self.assertTrue(self.test_admin.add_staff("new_staff", "secretpassword"))
        # Checking the result when trying to add someone that already exists
        self.assertFalse(self.test_admin.add_staff("jake", "s3cur3pa55w0rd"))

    def test_remove_staff(self):
        # Checking the result when trying to delete a staff that doesn't exist
        self.assertFalse(self.test_admin.remove_staff("barrybluejeans"))
        # Checking the result when trying to remove someone that does exist
        self.assertTrue(self.test_admin.remove_staff("new_staff"))

    def test_change_permissions(self):
        # Checking the result when trying to change an existing users permissions
        self.assertTrue(self.test_admin.change_permissions("jake", "user"))
        # Checking the result when trying to change a non existent users permissions
        self.assertFalse(self.test_admin.change_permissions("new_staff", "admin"))
        # Checking result when trying to change existing users permissions to the same permissions they already have
        self.assertFalse(self.test_admin.change_permissions("jake", "user"))

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
        # Checking if a flight with valid data can be added
        valid_flight = {"flight_reference": "SA 74", "flight_destination": "Paris",
                        "departure_location": "JFK", "flight_duration": 420, "departure_time": "10am",
                        "arrival_time": "5pm", "total_seats": 250
                        }
        self.assertTrue(self.test_admin.add_flight(valid_flight))
        # Checking if a flight with invalid data can be added
        invalid_flight = {"flight_reference": "APOLLO 11", "flight_destination": "Moon",
                          "departure_location": "Earth", "flight_duration": 9000, "departure_time": "10am",
                          "arrival_time": "5pm", "total_seats": 2
                          }
        self.assertFalse(self.test_admin.add_flight(invalid_flight))
