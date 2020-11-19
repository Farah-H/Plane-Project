from authentication import Authentication


class Staff(Authentication):
    def display_flight_id(self, flight_ref):
        data = []
        query = f"SELECT journey_details.journey_id, planes.plane_type, journey_details.departure_time, journey_details.arrival_time, journey_details.departing_from, journey_details.arriving_to, planes.plane_capacity, planes.seats_available, airports.country_code, country.additional_restrictions, country.visa_restrictions FROM journey_details INNER JOIN planes on journey_details.plane_id = planes.plane_id INNER JOIN airports on journey_details.arriving_to = airports.airport_code INNER JOIN country on airports.country_code = country.country_code"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                print(row)
                if flight_ref in row[0]:
                    data.append(row)
                row = self.cursor.fetchone()

        return data if len(data) > 0 else False

    def display_flight_destination(self, destination):
        data = []
        query = f"SELECT planes.plane_type, journey_details.departure_time, journey_details.arrival_time, journey_details.departing_from, journey_details.arriving_to, planes.plane_capacity, planes.seats_available, airports.country_code, country.additional_restrictions, country.visa_restrictions FROM journey_details INNER JOIN planes on journey_details.plane_id = planes.plane_id INNER JOIN airports on journey_details.arriving_to = airports.airport_code INNER JOIN country on airports.country_code = country.country_code"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                print(row)
                if destination in row[7]:
                    data.append(row)
                row = self.cursor.fetchone()

        return data if len(data) > 0 else False

    def display_flight_date(self, date):
        data = []
        query = f"SELECT planes.plane_type, journey_details.departure_time, journey_details.arrival_time, journey_details.departing_from, journey_details.arriving_to, planes.plane_capacity, planes.seats_available, airports.country_code, country.additional_restrictions, country.visa_restrictions FROM journey_details INNER JOIN planes on journey_details.plane_id = planes.plane_id INNER JOIN airports on journey_details.arriving_to = airports.airport_code INNER JOIN country on airports.country_code = country.country_code"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                check_date = row[1]
                if date.strftime("%Y-%m-%d") == check_date.strftime("%Y-%m-%d"):
                    data.append(row)
                row = self.cursor.fetchone()

        return data if len(data) > 0 else False

    def add_passenger(self, *args):
        pass

    def change_passenger(self, passport_id, column, new_data):
        query = f"UPDATE passenger_details SET {column} = '{new_data}' WHERE passport_id = '{passport_id}'"
        with self.cursor.execute(query):
            print("Successfully altered the flight information!")
        self.connection.commit()

    def display_passenger(self, fname, lname):
        data = []
        query = f"SELECT first_name, last_name, dob, passport_id, dependent_on FROM passenger_details"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                if fname.lower() == row[0] and lname.lower() == row[1]:
                    data.append(row)
                row = self.cursor.fetchone()

        return data if len(data) > 0 else False

    def security_check(self, flight_ref):
        pass
