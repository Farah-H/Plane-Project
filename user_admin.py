from authentication import Authentication
from user_staff import Staff
from db_backup import BackupData


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
        query = f"DELETE FROM credentials WHERE username = '{username}'"
        with self.cursor.execute(query):
            print("Successfully deleted the user!")
        self.connection.commit()

    def change_permissions(self, username, new_perm):
        query = f"UPDATE credentials SET permissions = '{new_perm}' WHERE username = '{username}'"
        with self.cursor.execute(query):
            print("Successfully altered user's permissions!")
        self.connection.commit()

    def view_user(self, username):
        data = None
        query = f"SELECT * FROM credentials WHERE username = '{username}'"
        with self.cursor.execute(query):
            data = self.cursor.fetchall()
        return data if data != None else False

    def add_flight(self, details):
        journey_columns = [
            "plane_id",
            "departure_time",
            "arrival_time",
            "departing_from",
            "arriving_to",
        ]
        journey_details = []
        for k, v in details.items():
            if k in journey_columns:
                journey_details.append(f"'{v}'")

        plane_query = f"INSERT INTO plane ({', '.join(journey_columns)}) VALUES ({', '.join(journey_details)})"
        print(plane_query)

    def edit_flight(self, flight_ref, column, new_data):
        pass

    def remove_flight(self, flight_ref):
        pass

    def add_plane(self, details):
        plane_columns = [
            "plane_type",
            "plane_capacity",
            "plane_size",
            "fuel_capacity",
            "speed",
            "weight",
            "seats_available",
            "fuel_per_km",
            "maintenance_data",
        ]
        plane_details = []
        for k, v in details.items():
            if k in plane_columns:
                plane_details.append(f"'{v}'")

        plane_query = f"INSERT INTO plane ({', '.join(plane_columns)}) VALUES ({', '.join(plane_details)})"
        print(plane_query)

    def edit_plane(self, flight_ref, column, new_data):
        pass

    def remove_plane(self, flight_ref):
        pass


def main():
    test = Admin("dev", "dev")
    plane_details = {
        "plane_type": "plane",
        "plane_capacity": 100,
        "plane_size": "M",
        "fuel_capacity": 120,
        "speed": 400,
        "weight": 12000,
        "seats_available": 37,
        "fuel_per_km": 12,
        "maintenance_data": "2020-08-11",
    }
    test.add_plane(plane_details)


if __name__ == "__main__":
    main()