from db_connection import Connection


class Guest(Connection):
    def __init__(self):
        super().__init__("guest", "guest")

    def all_flights(self):
        data = []
        query = "SELECT planes.plane_type, journey_details.departure_time, journey_details.arrival_time, journey_details.departing_from, journey_details.arriving_to, planes.plane_capacity, planes.seats_available, airports.country_code, country.additional_restrictions, country.visa_restrictions FROM journey_details INNER JOIN planes on journey_details.plane_id = planes.plane_id INNER JOIN airports on journey_details.departing_from = airports.airport_code INNER JOIN country on airports.country_code = country.country_code"
        count = 0
        with self.cursor.execute(query):
            row = self.cursor.fetchone()
            while row and count < 10:
                data.append(row)
                count += 1
                row = self.cursor.fetchone()
        return data if len(data) > 0 else False

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


def main():
    test = Guest()
    print(test.all_flights())


if __name__ == "__main__":
    main()