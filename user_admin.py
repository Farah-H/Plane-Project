from authentication import Authentication
from user_staff import Staff

### Admin can ###
# Do everything a Staff Member can
# Can add a new staff member
# Change Staff Permissions
# Can view all information (sensitive too)
# Can add / remove / edit all flight information


class Admin(Authentication):
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
    def edit_flight(self, flight_ref, **kwargs):
        # Returns True False
        pass

    # Same as above but takes all info as dict
    def add_flight(self, **kwargs):
        # True / False
        pass


def main():
    test = Admin("dev", "dev")
    test.add_staff("SomeUser", "Password")
    test.remove_staff("SomeUser")
    test.change_permissions("farah", "admin")
    print(test.view_user("dev"))


if __name__ == "__main__":
    main()