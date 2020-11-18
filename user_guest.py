from db_connection import Connection


class Guest(Connection):
    def __init__(self):
        # Establishes connection with "guest" credentials
        # Those credentials only have "read" access in the db
        super().__init__("guest", "guest")

    def all_flights(self):
        data = []
        query = "SELECT planes.plane_type, journey_details.departure_time, journey_details.arrival_time, journey_details.departing_from, journey_details.arriving_to, planes.plane_capacity, planes.seats_available FROM journey_details INNER JOIN planes on journey_details.plane_id = planes.plane_id"
        count = 0
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row and count < 10:
                data.append(row)
                count += 1
                row = self.cursor.fetchone()
        return data if len(data) > 0 else False

    # takes flight reference
    def display_flight(self, flight_ref):
        data = None
        query = f"SELECT planes.plane_type, journey_details.departure_time, journey_details.arrival_time, journey_details.departing_from, journey_details.arriving_to, planes.plane_capacity, planes.seats_available FROM journey_details INNER JOIN planes on journey_details.plane_id = planes.plane_id  WHERE journey_id = '{flight_ref}'"
        with self.cursor.execute(query):
            row = self.cursor.fetchall()
            data = row
        return data if data != None else False
