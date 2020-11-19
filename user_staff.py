from authentication import Authentication


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

    def add_passenger(self, *args):
        pass

    def change_passenger(self, *args):
        pass

    # NEEDS TO BE TESTED WITH MULTIPLE CASES!
    def display_flight(self, var, arg):
        data = []
        if var == "journey_details.departure_time":
            arg = "-".join(arg)
        query = f"SELECT planes.plane_type, journey_details.departure_time, journey_details.arrival_time, journey_details.departing_from, journey_details.arriving_to, planes.plane_capacity, planes.seats_available, airports.country_code, country.additional_restrictions, country.visa_restrictions FROM journey_details INNER JOIN planes on journey_details.plane_id = planes.plane_id INNER JOIN airports on journey_details.departing_from = airports.airport_code INNER JOIN country on airports.country_code = country.country_code"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                if arg in row:
                    data.append(row)
                row = self.cursor.fetchone()

        return data if len(data) > 0 else False

    # PLACEHOLDER
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
