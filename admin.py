import pyodbc
import json
import hashlib
import os
import binascii


class Connection:
    def __init__(self, db_login, db_password):
        self.server = "82.34.117.17"
        self.database = "plane_project"
        self.username = db_login
        self.password = db_password
        self.connection = pyodbc.connect(
            f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
        )
        self.cursor = self.connection.cursor()


class BackupData(Connection):
    def __init__(self, db_login, db_password, table_name, backup_file):
        super().__init__(db_login, db_password)
        self.table_name = table_name
        self.backup_file = backup_file

    def backup_handler(self):
        try:
            sql_data = self.pull_table(self.table_name)
        except:
            print(
                "Unable to load the SQL table.\nCheck that the table name provided exists."
            )
        else:
            try:
                old_data = self.load_file(self.backup_file)
            except:
                print("The backup file does not exist.\nSkipping loading old Data.")
            finally:
                self.constructor(self.backup_file, sql_data)

        return old_data

    def pull_table(self, table_name):
        data = []
        query = f"SELECT * FROM {table_name}"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                data.append(row)
                row = self.cursor.fetchone()
        return data

    def load_file(self, file):
        with open(file, "r") as file_data:
            data = json.load(file_data)
        return data

    def constructor(self, file, export_data):
        with open(file, "w") as file_data:
            json.dump(export_data, file_data, indent=4, sort_keys=True)


class StaffMember(Connection):
    def __init__(self, login, password, required_permissions):
        self.__login = login
        self.__password = password
        self.__required_permissions = required_permissions

    def change_password(self, username, new_password):
        query = f"SELECT * FROM credentials"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                if username == row[1]:
                    password = hashpass(new_password)
                    query = f"UPDATE credentials SET {row[2]} = ? WHERE username = ?"
                    with self.cursor.execute(query, password, username):
                        print("Password updated successfully!")
                    self.connection.commit()
                    break
                row = self.cursor.fetchone()

    def check_login(self, login, password, permissions):
        # Check login details and Staff Permission Level
        pass

    def password(self, new_password):
        pwd = self.hashpass(new_password)

        ####### REPLACE WITH SQL REQUEST #######
        data = self.get_data("passwords.json")
        data[self.account_number] = pwd
        self.constructor("passwords.json", data)
        ########################################

    def hashpass(self, password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
        pwd_hash = hashlib.pbkdf2_hmac("sha512", password.encode("utf-8"), salt, 100000)
        pass_hash = binascii.hexlify(pwd_hash)
        return (salt + pass_hash).decode("ascii")

    def checkhash(self, stored_pwd, given_pwd):
        salt = stored_pwd[:64]
        stored_pwd = stored_pwd[64:]
        pwd_hash = hashlib.pbkdf2_hmac(
            "sha512", given_pwd.encode("utf-8"), salt.encode("ascii"), 100000
        )
        pass_hash = binascii.hexlify(pwd_hash).decode("ascii")

        return pass_hash == stored_pwd