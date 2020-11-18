class Flight:
    def __init__(self, airline_id, airline_name, from_location, to_location, departure_timme, arrival_time, flight_duration, total_seats):
        self.airline_id = airline_id
        self.airline_name = airline_name
        self.from_location = from_location
        self.to_location = to_location
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.flight_duration = flight_duration
        self.total_seats = total_seats

# the ui.py will interact with a user retrieve the required info
# to accomplish a User Story 

def body():

    # prompt the user to enter login details to access the booking system
    print("Please login to continue")
    username = input("Username:\n")
    password = input("Password:\n")

    while True:
        print("""\nPick an option:
                    1. Passenger booking manager
                    2. Flight manager
                    3. EXIT"""
        # if the user inputs an invalid option the code runs again
        try:
            choice_0 = int(input("--->  "))
        except:
            continue
    

    if choice_0 == 1:
        while True:
        print("""\nPick an option:
                    1. Make a booking
                    2. Change the details of an existing booking
                    3. Cancel a booking
                    3. EXIT"""
        
        # if the user inputs an invalid option the code runs again
        try:
            choice_1 = int(input("--->  "))
        except:
            continue
    


    elif choice_0 == 2:
        while True:
        print("""\nPick an option:
                    1. Make a flight route
                    2. View flight routes
                    3. EXIT"""
        
        # if the user inputs an invalid option the code runs again
        try:
            choice_1 = int(input("--->  "))
        except:
            continue
    
    
    
    if choice_1 == 1:
        while True:
            print("\nIn order to make a booking, please answer the following questions: ")
            fname = input("Enter passenger first name:\n ").title()
            lname = input("Enter passenger last name:\n ").title()
            p_number = input("Enter passenger passport number:\n ")
            dob = input("Enter passenger date of birth as DD/MM/YYYY:\n ")
            home_address = input("Enter passenger home address:\n ")
            email_address = input("Enter passenger email address:\n ")
            telephone = input("Enter passenger telephone number:\n ")
            
            choice_1_1 = input("YES or NO\nIs the passenger travelling with a minor? ").lower()
            if choice_1_1 == "yes":
                minor_number = input("How many minors are you travelling with:\n ").int()
                for i in range(0, minor_number):
                    min_fname = input("Enter the minor first name:\n ").title()
                    min_lname = input("Enter the minor last name:\n ").title()
                    min_p_number = input("Enter the minor passport number :\n ")
                    min_dob = input("Enter the minor date of birth as DD/MM/YYYY:\n ")
                    min_home_address = input("Enter the minor home address:\n ")
            elif choice_1_1 =="no":
                continue
            departure_date = input("")
            
            # list of cities and countries combined
            atlas = [] 
            
            # from_location existence is verified
            from_location = input("Where will you be travelling from?\n")
            if from_location in atlas:
                continue
            else:
                print("Please enter a valid departure location.")
            
            # from_location existence is verified
            to_location = input("Where will you be travelling to?\n")
            if from_location in atlas:
                continue
            else:
                print("Please enter a valid destination location.")

    elif choice_1 == 2:
        while True:
    