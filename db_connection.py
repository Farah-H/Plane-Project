import pyodbc
import json


class Connection:
    def __init__(self, db_login, db_password):
        self.__server = "82.34.117.17"
        self.__database = "plane_project"
        self.__username = db_login
        self.__password = db_password
        self.connection = pyodbc.connect(
            f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.__server};DATABASE={self.__database};UID={self.__username};PWD={self.__password}"
        )
        self.cursor = self.connection.cursor()
