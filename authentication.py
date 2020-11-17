import hashlib
import os
import binascii
from db_connection import Connection


class Authentication(Connection):
    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.__can_login = self.check_login(self.__login, self.__password)
        self.__credential_list = self.db_credentials(self.__can_login)
        self.__db_login = self.__credential_list[0]
        self.__db_password = self.__credential_list[0]
        self.__permission_level = self.__credential_list[1]
        super().__init__(self.__db_login, self.__db_password)

    @property
    def permission_level(self):
        return self.__permission_level

    def db_credentials(self, can_login):
        if can_login != False:
            return self.__login, can_login
        else:
            raise Exception("Error: Login credentials do not match the db.")

    def credential_manager(self, username):
        query = f"SELECT * FROM credentials"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                if username == row[1]:
                    return row
                row = self.cursor.fetchone()
        return False

    def check_login(self, login, password):
        data = self.credential_manager(login)

        if isinstance(data, list):
            if checkhash(data[2], password):
                return data[3]
        return False

    def password(self, username, new_password):
        data = self.credential_manager(username)

        if isinstance(data, list):
            password = hashpass(new_password)
            query = f"UPDATE credentials SET {data[2]} = ? WHERE username = ?"
            with self.cursor.execute(query, password, username):
                print("Password updated successfully!")
            self.connection.commit()
            return True
        return False

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
