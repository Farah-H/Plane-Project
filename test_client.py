from client import ClientInformation
import unittest
import pytest


class TestClient(unittest.TestCase):
    test_client = ClientInformation("Mr.", "Jeff", "Bridges", "64 Zoo Lane", "05/11/1958")
    # Testing the Client properties return the correct information
    def test_init__(self):
        self.assertEqual(self.test_client.title, "Mr.")
        self.assertEqual(self.test_client.first_name, "Jeff")
        self.assertEqual(self.test_client.last_name, "Bridges")
        self.assertEqual(self.test_client.address, "64 Zoo Lane")
        self.assertEqual(self.test_client.full_name, "Mr. Jeff Bridges")
