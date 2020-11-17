import hashlib
import os
import binascii
from db_connection import Connection


class Authentication(Connection):
    def __init__(self, login, password, required_permissions):
        self.__login = login
        self.__password = password
        self.__required_permissions = required_permissions
        self.__can_login = check_login(
            self.__login, self.__password, self.__required_permissions
        )
        self.__db_login = db_credentials(self.__can_login, self.__required_permissions)
        self.__db_password = db_credentials(
            self.__can_login, self.__required_permissions
        )
        super().__init__(self.__db_login, self.__db_password)

    def db_credentials(self, can_login, permission):
        if can_login:
            if permission == "admin":
                return "dev"
            elif permission == "user":
                return self.__login
            else:
                raise Exception("Error: Permission level doesn't exist.")
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

    def check_login(self, login, password, permissions):
        data = self.credential_manager(login)

        if isinstance(data, list):
            if checkhash(data[2], password):
                if data[3] == permissions:
                    return True
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
