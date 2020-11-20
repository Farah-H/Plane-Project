from db_connection import Connection
from datetime import datetime


class Guest(Connection):
    def __init__(self):
        super().__init__("guest", "guest")

    def all_flights(self):
        data = []
        query = "SELECT planes.plane_type, journey_details.departure_time, journey_details.arrival_time, journey_details.departing_from, journey_details.arriving_to, planes.plane_capacity, planes.seats_available, airports.country_code, country.additional_restrictions, country.visa_restrictions FROM journey_details INNER JOIN planes on journey_details.plane_id = planes.plane_id INNER JOIN airports on journey_details.arriving_to = airports.airport_code INNER JOIN country on airports.country_code = country.country_code"
        count = 0
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row and count < 10:
                data.append(row)
                count += 1
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
