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

    def change_passenger(self, passport_id, column, new_data):
        query = f"UPDATE passenger_details SET {column} = '{new_data}' WHERE passport_id = '{passport_id}'"
        with self.cursor.execute(query):
            print("Successfully altered the passenger's information!")
        self.connection.commit()

    def display_passenger(self, fname, lname):
        data = []
        query = f"SELECT first_name, last_name, dob, passport_id, dependent_on FROM passenger_details"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                if fname.lower() in row[0].lower() and lname.lower() in row[1].lower():
                    data.append(row)
                row = self.cursor.fetchone()

        return data if len(data) > 0 else False

    def security_check(self, flight_ref):
        data = []
        query = f"SELECT passenger_details.first_name, passenger_details.last_name, passenger_details.dob, passenger_details.passport_id FROM passenger_details INNER JOIN ticket_details on ticket_details.passenger_id = passenger_details.passenger_id WHERE ticket_details.journey_id = '{flight_ref}';"
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row:
                data.append(row)
                row = self.cursor.fetchone()

        return data if len(data) > 0 else False

    def add_passport(self, passport_id, issue_date, expiry_date, expired, country_code):
        check_query = "SELECT * FROM passport_details"
        exists = False
        with self.cursor.execute(check_query):
            row = self.cursor.fetchone()
            while row:
                if passport_id in row[0]:
                    exists = True
                row = self.cursor.fetchone()

        if not exists:
            query = f"INSERT INTO passport_details (passport_id, issue_date, [expiry_date], expired, country_code) VALUES ('{passport_id}', '{issue_date}', '{expiry_date}', '{expired}', '{country_code}');"
            self.cursor.execute(query)
            self.cursor.commit()

    def add_passenger(self, passport_id, fname, lname, dob, dependent):
        check_query = "SELECT * FROM passenger_details"
        exists = False
        with self.cursor.execute(check_query):
            row = self.cursor.fetchone()
            while row:
                if passport_id in row:
                    exists = row[0]
                row = self.cursor.fetchone()

        if exists == False:
            if dependent != "NULL":
                dependent = f"'{dependent}'"

            query = f"INSERT INTO passenger_details (passport_id, first_name, last_name, dob, dependent_on) VALUES ('{passport_id}', '{fname}', '{lname}', '{dob}', {dependent});"
            self.cursor.execute(query)
            self.cursor.commit()

            check_query = "SELECT * FROM passenger_details"
            exists = False
            with self.cursor.execute(check_query):
                row = self.cursor.fetchone()
                while row:
                    if passport_id in row:
                        exists = row[0]
                    row = self.cursor.fetchone()
            return exists
        else:
            return exists

    def add_booking(self, booking_date, staff_id, airline, price):
        query = f"INSERT INTO booking_details (booking_date, staff_id, airline, total) VALUES ( '{booking_date}', '{staff_id}', '{airline}', '{price}');"
        self.cursor.execute(query)
        self.cursor.commit()

        return_query = "SELECT * FROM booking_details"
        with self.cursor.execute(return_query):
            data = self.cursor.fetchall()
        return data[-1][0]

    def add_ticket(
        self, journey_id, seat_number, terminal_id, passenger_id, booking_id
    ):
        query = f"INSERT INTO ticket_details(journey_id, seat_number, terminal_id, passenger_id, booking_id) VALUES ('{journey_id}', '{seat_number}', '{terminal_id}', '{passenger_id}', '{booking_id}');"
        self.cursor.execute(query)
        self.cursor.commit()
