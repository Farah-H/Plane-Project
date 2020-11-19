from authentication import Authentication
from datetime import datetime


class Staff(Authentication):
    def display_flight_id(self, flight_ref):
        data = []
        query = f"SELECT journey_details.journey_id, planes.plane_type, journey_details.departure_time, journey_details.arrival_time, journey_details.departing_from, journey_details.arriving_to, planes.plane_capacity, planes.seats_available, airports.country_code, country.additional_restrictions, country.visa_restrictions FROM journey_details INNER JOIN planes on journey_details.plane_id = planes.plane_id INNER JOIN airports on journey_details.arriving_to = airports.airport_code INNER JOIN country on airports.country_code = country.country_code WHERE journey_details.journey_id = {flight_ref}"
        with self.cursor.execute(query):
            data = self.cursor.fetchall()
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

    def add_passengers(
        self, journey_id, staff_id, airline, date, terminal, user_data, price
    ):
        for i in range(len(user_data)):
            user_data[i] = f"'{user_data[i]}'"

        journey_id = f"'{journey_id}'"
        staff_id = f"'{staff_id}'"
        airline = f"'{airline}'"
        date = f"'{date}'"
        terminal = f"'{terminal}'"
        price = f"'{price}'"

        passport_query = f"INSERT INTO passport_details (passport_id, issue_date, expiry_date, expired, country_code) VALUES ('{user_data[0]}', 'NULL', 'NULL', '0', 'UK')"
        self.cursor.execute(passport_query)
        self.connection.commit()

        passenger_query = f"INSERT INTO passenger_details (passport_id, first_name, last_name, dob, dependent_on) VALUES ({', '.join(user_data[-1])}"
        self.cursor.execute(passenger_query)
        self.connection.commit()

        booking_query = f"INSERT INTO booking_details (booking_date, staff_id, airline, total) VALUES ('{date}', '{staff_id}', '{airline}', '{price}')"
        self.cursor.execute(passenger_query)
        self.connection.commit()

        booking_id_query = f"SELECT * FROM booking_details"
        booking_id = None
        with self.cursor.execute(booking_id_query):
            row = self.cursor.fetchone()
            while row:
                if row[2] == date:
                    booking_id = row[0]
                row = self.cursor.fetchone()

        if booking_id != None:
            passenger_id_query = f"SELECT * FROM passenger_details"
            passenger_id = None
            with self.cursor.execute(passenger_id_query):
                row = self.cursor.fetchone()
                while row:
                    if user_data[1] == row[2] and user_data[2] == row[3]:
                        passenger_id = row[0]
                    row = self.cursor.fetchone()

            if passenger_id != None:
                ticket_query = f"INSERT INTO ticket_details (journey_id, seat_number, termianal_id, passenger_id, booking_id) VALUES ('{journey_id}', '{user_data[-1]}', 'NULL', '{passenger_id}', '{booking_id}')"

                self.cursor.execute(passenger_query)
                self.connection.commit()
            else:
                raise Exception()

        else:
            raise Exception()

    def add_single_passenger(self, user_data):
        for i in range(len(user_data)):
            user_data[i] = f"'{user_data[i]}'"

        journey_id, staff_id, airline, date, terminal, price = (
            user_data[0],
            user_data[1],
            user_data[2],
            user_data[3],
            user_data[4],
            user_data[-1],
        )

        passport_query = f"INSERT INTO passport_details (passport_id, issue_date, expiry_date, expired, country_code) VALUES ({user_data[5]}, '2017-03-02', '2020-09-01', '0', 'UK')"
        self.cursor.execute(passport_query)
        self.connection.commit()

        passenger_query = f"INSERT INTO passenger_details (passport_id, first_name, last_name, dob, dependent_on) VALUES ({', '.join(user_data[5:-2])}, NULL)"
        self.cursor.execute(passenger_query)
        self.connection.commit()

        booking_query = f"INSERT INTO booking_details (booking_date, staff_id, airline, total) VALUES ({date}, {staff_id}, {airline}, {price})"
        self.cursor.execute(passenger_query)
        self.connection.commit()

        booking_id_query = f"SELECT * FROM booking_details"
        booking_id = None
        with self.cursor.execute(booking_id_query):
            row = self.cursor.fetchone()
            while row:
                if date in str(row[2]):
                    booking_id = row[0]
                row = self.cursor.fetchone()

        if booking_id != None:
            passenger_id_query = f"SELECT * FROM passenger_details"
            passenger_id = None
            with self.cursor.execute(passenger_id_query):
                row = self.cursor.fetchone()
                while row:
                    if user_data[1] in str(row[2]) and user_data[2] in str(row[3]):
                        passenger_id = row[0]
                    row = self.cursor.fetchone()

            if passenger_id != None:
                ticket_query = f"INSERT INTO ticket_details (journey_id, seat_number, termianal_id, passenger_id, booking_id) VALUES ('{journey_id}', '{user_data[-1]}', 'NULL', '{passenger_id}', '{booking_id}')"

                self.cursor.execute(passenger_query)
                self.connection.commit()

    def remove_passenger(self):
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
        data = []
        query = f"SELECT ticket_details.ticket_id, ticket_details.seat_number, passenger_details.first_name, passenger_details.last_name, passenger_details.passport_id, passenger_details.dependent_on from passenger_details inner join ticket_details on passenger_details.passenger_id = ticket_details.passenger_id WHERE ticket_details.booking_id = {flight_ref}"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                data.append(row)
                row = self.cursor.fetchone()

        return data if len(data) > 0 else False
