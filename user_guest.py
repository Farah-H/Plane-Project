from db_connection import Connection

##### PLACEHOLDER #####
# Guest Functionality #
#######################


class Guest(Connection):
    def __init__(self):
        # Establishes connection with "guest" credentials
        # Those credentials only have "read" access in the db
        super().__init__("guest", "guest")

    def get_table(self, table_name):
        data = []
        query = f"SELECT * FROM {table_name}"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                data.append(row)
                row = self.cursor.fetchone()
        return data