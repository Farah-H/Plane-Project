from db_connection import Connection

##### PLACEHOLDER #####
# Guest Functionality #
#######################


class Guest(Connection):
    def __init__(self):
        # Establishes connection with "guest" credentials
        # Those credentials only have "read" access in the db
        super().__init__("guest", "guest")

    def all_flights(self):
        data = []
        query = "SELECT * FROM journey_details"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                data.append(row)
                row = self.cursor.fetchone()
        return data if len(data) > 0 else False

    # takes flight reference
    def display_flight(self, flight_ref):
        data = None
        query = f"SELECT * FROM journey_details WHERE journey_id = '{flight_ref}'"
        with self.cursor.execute(query):
            row = self.cursor.fetchall()
            data = row
        return data if data != None else False

    ###########################
    # PLACE HOLDER DO NOT USE #
    ###########################
    def get_table(self, table_name):
        data = []
        query = f"SELECT * FROM {table_name}"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                data.append(row)
                row = self.cursor.fetchone()
        return data if len(data) > 0 else False