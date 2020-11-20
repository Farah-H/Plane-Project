from db_backup import BackupData
import unittest
import pytest


class TestBackup(unittest.TestCase):
    test_backup = BackupData("jake", "jake", "ticket_details", ticket_backup.json)
    test_backup_invalid = BackupData("jake", "jake", "ticket_detailz", ticket_notbackup.json)

    def test_pull_data(self):
        # Checking that at least one row of data has been retrieved from the ticket_details table in the database
        self.assertNotEqual(self.test_backup.pull_data("ticket_details"), [])

    def test_load_file(self):
        # Checking if an exception is raised when trying to load data from a non existent file
        self.assertRaises(IOError, self.test_backup.load_data(ticket_backup17.json))
        # Checking that it can load data from the provided file (this will always be not none but idk what to test?)
        self.assertIsNotNone(self.test_backup.load_data(ticket_backup.json))

    def test_constructor(self):
        # Checking if an exception is raised when trying to dump data??
        self.assertRaises(IOError, self.test_backup.constructor(ticket_backup17.json, ))

    def test_backup_handler(self):
        # Checking if None is returned when called from an instance that holds incorrect table and file information
        self.assertIsNone(self.test_backup_invalid.backup_handler())
        # Checking if actual data is returned when called from an instance that holds correct table and file information
        self.assertIsNotNone(self.test_backup.backup_handler())
