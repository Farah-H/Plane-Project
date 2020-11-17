class Flight:
    def __init__(self, airline_id, airline_name, from_location, to_location, departure_timme, arrival_time, flight_duration, total_seats):
        self.airline_id = airline_id
        self.airline_name = airline_name
        self.from_location = from_location
        self.to_location = to_location
        self.departure_timme = departure_timme
        self.arrival_time = arrival_time
        self.flight_duration = flight_duration
        self.total_seats = total_seats
    
def body():
        while True:
            print("""\nPick an option:
                        1. I am a passenger
                        2. I am a staff member
                        3. EXIT"""
            # ff the user inputs an invalid option the code reruns
            try:
                choice_0 = int(input("--->  "))
            except:
                continue
        
        if choice_0 == 1:
            while True:
            print("""\nPick an option:
                        1. Make a booking
                        2. Change an existing booking
                        3. EXIT"""
            # if the user inputs an invalid option the code reruns
            try:
                choice_1 = int(input("--->  "))
            except:
                continue
        
        elif choice_0 == 2:
            print("Please login to continue")
            username = input("")
            password = input("")

        if choice_1 == 1:
            while True:
                print("\nIn order to make a booking, please answer the following questions: ")
                fname = input("Enter your first name:\n ").title()
                lname = input("Enter your last name:\n ").title()
                p_number = input("Enter your passport number :\n ")
                dob = input("Enter your date of birth as DD/MM/YYYY:\n ")
                home_address = input("Enter your home address:\n ")
                email_address = input("Enter your email address:\n ")
                telephone = input("Enter your telephone number:\n ")
                choice_1_1 = input("YES or NO\nAre you travelling with a minor? ").lower()
                if choice_1_1 == "yes":
                    min_fname = input("Enter the minor first name:\n ").title()
                    min_lname = input("Enter the minor last name:\n ").title()
                    min_p_number = input("Enter the minor passport number :\n ")
                    min_dob = input("Enter the minor date of birth as DD/MM/YYYY:\n ")
                    min_home_address = input("Enter the minor home address:\n ")

        elif choice_1 == 2:
            while True:
        
