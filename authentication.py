import hashlib
import os
import binascii
from db_connection import Connection


class Authentication(Connection):
    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.__can_login = self.check_login(self.__login, self.__password)
        # List that stores two return values
        self.__credential_list = self.db_credentials(self.__can_login)
        # This is used for DB Connection
        self.__db_login = self.__credential_list[0]
        self.__db_password = self.__credential_list[0]
        # This is our staff member's permission level
        self.__permission_level = self.__credential_list[1]
        super().__init__(self.__db_login, self.__db_password)

    # Property for getting the Staff member's permission level
    @property
    def permission_level(self):
        return self.__permission_level

    def db_credentials(self, can_login):
        # If not a boolean (it must be a string)
        if can_login != False:
            # Returns login and permission level as a string
            return self.__login, can_login
        else:
            # If cannot login then raises an error (stops class from initialising)
            raise Exception("Error: Login credentials do not match the db.")

    # Function for pulling all credentials and returing only the selected username's information
    def credential_manager(self, username):
        query = f"SELECT * FROM credentials"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                if username == row[1]:
                    # Returns a List (if username found)
                    return row
                row = self.cursor.fetchone()
        # OR returns a boolean if username not found
        return False

    # Function for checking if username exists and password matches
    def check_login(self, login, password):
        data = self.credential_manager(login)

        if isinstance(data, list):
            if checkhash(data[2], password):
                # Returns a String
                return data[3]
        # OR returns a boolean
        # If password does not match
        # If 'data' returned is a boolean (username not found)
        return False

    # Function for changing the password
    def password(self, username, new_password):
        data = self.credential_manager(username)

        # Checks if data exists (is list)
        if isinstance(data, list):
            # Creates a hash of the new password
            password = hashpass(new_password)
            # Updates that password into db
            query = f"UPDATE credentials SET {data[2]} = ? WHERE username = ?"
            with self.cursor.execute(query, password, username):
                print("Password updated successfully!")
            # Commits that change to the DB
            self.connection.commit()
            # Returns true if successful
            return True
        # Returns false if unsuccessful
        return False

    # Function for hashing the password
    def hashpass(self, password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
        pwd_hash = hashlib.pbkdf2_hmac("sha512", password.encode("utf-8"), salt, 100000)
        pass_hash = binascii.hexlify(pwd_hash)
        # Returns the password hash as String
        return (salt + pass_hash).decode("ascii")

    # Function for comparing passwords
    def checkhash(self, stored_pwd, given_pwd):
        salt = stored_pwd[:64]
        stored_pwd = stored_pwd[64:]
        pwd_hash = hashlib.pbkdf2_hmac(
            "sha512", given_pwd.encode("utf-8"), salt.encode("ascii"), 100000
        )
        pass_hash = binascii.hexlify(pwd_hash).decode("ascii")
        # Returns a Boolean
        return pass_hash == stored_pwd
