from authentication import Authentication
from user_staff import Staff
from db_backup import BackupData
from datetime import datetime


class Admin(Staff):
    def backup_table(self, table_name, file_name):
        back_up = BackupData(self.db_login, self.db_login, table_name, file_name)
        data = back_up.backup_handler()
        return data if data != None else False

    def add_staff(self, username, password):
        password = self.hashpass(password)
        query = f"INSERT INTO credentials (username, password, permissions) VALUES ('{username}', '{password}', 'user')"
        with self.cursor.execute(query):
            print("Succesfully added the user!")
        self.connection.commit()

    def remove_staff(self, username):
        check = "SELECT * FROM credentials"
        with self.cursor.execute(check):
            row = self.cursor.fetchone()
            while row:
                if username in row:
                    found = True
                row = self.cursor.fetchone()

        if found:
            query = f"DELETE FROM credentials WHERE username = '{username}'"
            with self.cursor.execute(query):
                print("Successfully deleted the user!")
            self.connection.commit()
        else:
            raise Exception()

    def change_permissions(self, username, new_perm):
        check = "SELECT * FROM credentials"
        with self.cursor.execute(check):
            row = self.cursor.fetchone()
            while row:
                if username in row:
                    found = True
                row = self.cursor.fetchone()

        if found:
            query = f"UPDATE credentials SET permissions = '{new_perm}' WHERE username = '{username}'"
            with self.cursor.execute(query):
                print("Successfully altered user's permissions!")
            self.connection.commit()
        else:
            raise Exception()

    def view_user(self, username):
        data = None
        query = f"SELECT * FROM credentials WHERE username = '{username}'"
        with self.cursor.execute(query):
            data = self.cursor.fetchall()
        return data if len(data) > 0 else False

    def add_flight(self, details, columns):
        journey_details = []
        for k, v in details.items():
            if k in columns:
                journey_details.append(f"'{v}'")

        flight_query = f"INSERT INTO journey_details ({', '.join(columns)}) VALUES ({', '.join(journey_details)})"
        with self.cursor.execute(flight_query):
            print("Succesfully added the plane!")
        self.connection.commit()

    def edit_flight(self, flight_ref, column, new_data):
        query = f"UPDATE journey_details SET {column} = '{new_data}' WHERE journey_id = '{flight_ref}'"
        with self.cursor.execute(query):
            print("Successfully altered the flight information!")
        self.connection.commit()

    def remove_flight(self, flight_ref):
        check = "SELECT * FROM journey_details"
        with self.cursor.execute(check):
            row = self.cursor.fetchone()
            while row:
                if flight_ref in row:
                    found = True
                row = self.cursor.fetchone()

        if found:
            query = f"DELETE FROM journey_details WHERE journey_id = '{flight_ref}'"
            with self.cursor.execute(query):
                print("Successfully deleted the flight!")
            self.connection.commit()
        else:
            raise Exception()

    def add_plane(self, details, columns):
        plane_details = []
        for k, v in details.items():
            if k in columns:
                plane_details.append(f"'{v}'")

        plane_query = f"INSERT INTO planes ({', '.join(columns)}) VALUES ({', '.join(plane_details)})"
        with self.cursor.execute(plane_query):
            print("Succesfully added the plane!")
        self.connection.commit()

    def edit_plane(self, plane_ref, column, new_data):
        query = (
            f"UPDATE planes SET {column} = '{new_data}' WHERE plane_id = '{plane_ref}'"
        )
        with self.cursor.execute(query):
            print("Successfully altered the plane information!")
        self.connection.commit()

    def remove_plane(self, plane_ref):
        check = "SELECT * FROM planes"
        with self.cursor.execute(check):
            row = self.cursor.fetchone()
            while row:
                if plane_ref in row:
                    found = True
                row = self.cursor.fetchone()

        if found:
            query = f"DELETE FROM planes WHERE plane_id = '{plane_ref}'"
            with self.cursor.execute(query):
                print("Successfully deleted the plane!")
            self.connection.commit()
        else:
            raise Exception()
