from db_connection import Connection


class Guest(Connection):
    def __init__(self):
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