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
    def add_passenger(self, *args):
        # Will return flight confirmation details
        # Probably list
        pass

    # Takes user full name + info to change + that new info
    def change_passenger(self, *args):
        # Returns True or False
        # If changed or failed to change
        pass

    # Takes Flight Referenece (string)
    def display_flight(self, flight_ref):
        data = None
        query = f"SELECT planes.plane_type, journey_details.departure_time, journey_details.arrival_time, journey_details.departing_from, journey_details.arriving_to, planes.plane_capacity, planes.seats_available FROM journey_details INNER JOIN planes on journey_details.plane_id = planes.plane_id  WHERE journey_id = '{flight_ref}'"
        with self.cursor.execute(query):
            row = self.cursor.fetchall()
            data = row

        # Example output:
        # [ plane type, departure time, arrival time, departing from, arriving to, plane capacity, seats available]
        # ["helicopter", "2020-11-11 13:23:44.000", "2020-11-11 15:23:44.000", "LHR", "LHR", 10, 1]
        return data if data != None else False

    # PLACEHOLDER
    # Takes full name 2x string
    def display_passenger(self, fname, lname):
        output = None
        data = self.get_data("passanger?")
        if data != False:
            for row in data:
                if row[0] == fname and row[1] == lname:
                    output.append(row)

        return output

    def security_check(self, flight_ref):
        pass
