from db_connection import Connection
import pyodbc
import unittest
import pytest


class TestConnection(unittest.TestCase):
    def test_conn(self):
        # Checking if the object is instantiated correctly, and therefore that the connection was established
        test = Connection("jake", "jake")
        self.assertIsInstance(test, Connection)
