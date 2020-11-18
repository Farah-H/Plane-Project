from db_backup import BackupData
import unittest
import pytest


class TestBackup(unittest.TestCase):
    test_backup = BackupData("jake", "jake", "ticket_details", ticket_backup.json)

    def test_pull_data(self):
        pass

    def test_load_file(self):
        pass

    def test_constructor(self):
        pass

    def test_backup_handler(self):
        pass