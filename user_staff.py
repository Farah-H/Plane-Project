from authentication import Authentication

### Staff can ###
# Add new passanger to flight
# Check specific information about the flight
# Check available spaces of a flight
# Remove passanger from the flight
# Change personal information about passanger
# Change any information about self
#
# CANNOT view sensitive information about the passanger


class Staff(Authentication):
    # Loads table data
    def get_data(self, table_name):
        data = []
        query = f"SELECT * FROM {table_name}"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                data.append(row)
                row = self.cursor.fetchone()
        return data if len(data) > 0 else False

    # No idea what information goes in ask Jake
    def add_passanger(self, *args):
        # Will return flight confirmation details
        # Probably list
        pass

    # Takes user full name + info to change + that new info
    def change_passanger(self, *args):
        # Returns True or False
        # If changed or failed to change
        pass

    # PLACEHOLDER
    # Takes Flight Referenece (string)
    def display_flight(self, flight_ref):
        data = self.get_data("name pending")
        return data

    # PLACEHOLDER
    # Takes full name 2x string
    def display_passanger(self, fname, lname):
        output = None
        data = self.get_data("passanger?")
        if data != False:
            for row in data:
                if row[0] == fname and row[1] == lname:
                    output.append(row)

        return output

    # Takes string
    def check_seats(self, flight_ref):
        # Returns integer
        pass
