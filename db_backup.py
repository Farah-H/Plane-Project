import json
from db_connection import Connection

#### PLACEHOLDER ####
# DOES NOT WORK YET #
#####################


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
