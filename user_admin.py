from authentication import Authentication
from user_staff import Staff
from db_backup import BackupData

### Admin can ###
# Do everything a Staff Member can
# Can add a new staff member
# Change Staff Permissions
# Can view all information (sensitive too)
# Can add / remove / edit all flight information


class Admin(Staff):
    def backup_table(self, table_name, file_name):
        back_up = BackupData(self.db_login, self.db_login, table_name, file_name)
        data = back_up.backup_handler()
        return data if data != None else False

    # These are self explanatory
    def add_staff(self, username, password):
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

    # View's all information about user
    def view_user(self, username):
        data = None
        query = f"SELECT * FROM credentials WHERE username = '{username}'"
        with self.cursor.execute(query):
            data = self.cursor.fetchall()
        return data if data != None else False

    # takes flight number string
    # and any new information as dictionary
    def edit_flight(self, **kwargs):
        pass

    # Same as above but takes all info as dict
    def add_flight(self, details):
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
        journey_columns = []
        plane_details = []
        journey_details = []
        for k, v in details.items():
            if k in plane_columns:
                plane_details.append(v)
            elif k in journey_columns:
                journey_details.append(v)

        plane_query = f"INSERT INTO plane ({', '.join(plane_columns)}) VALUES ("
        print(plane_query)

    def remove_flight(self, flight_ref):
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
    test.add_flight(plane_details, "hi")


if __name__ == "__main__":
    main()