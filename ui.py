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
                    3. EXIT""")
        # if the user inputs an invalid option the code runs again
        try:
            choice_0 = int(input("--->  "))
            try: 
                if choice_0 in range(1, 4):
                    continue
            except:
                continue
        except:
            continue
    

    if choice_0 == 1:
        while True:
            print("Welcome to the booking manager.")
            print("""\nPick an option:
                    1. Make a booking
                    2. Change the details of an existing booking
                    3. Cancel a booking
                    4. EXIT""")
        
        # if the user inputs an invalid option the code runs again
        try:
            choice_0_1= int(input("--->  "))
            try: 
                if choice_0_1 in range(1, 5):
                    continue
            except:
                continue
        except:
            continue
    
    # user is prompted to enter information required to make a booking
    if choice_0_1 == 1:
        while True:
            print("\nIn order to make a booking, please answer the following questions: ")
            fname = input("Enter passenger first name:\n ").title()
            lname = input("Enter passenger last name:\n ").title()
            p_number = input("Enter passenger passport number:\n ")
            dob = input("Enter passenger date of birth as DD/MM/YYYY:\n ")
            home_address = input("Enter passenger home address:\n ")
            email_address = input("Enter passenger email address:\n ")
            telephone = input("Enter passenger telephone number:\n ")
            
            # accompanied minor or minors will also need to input details
            choice_0_1_1 = input("YES or NO\nIs the passenger travelling with a minor? ").lower()
            if choice_0_1_1 == "yes":
                minor_number = input("How many minors are you travelling with:\n ").int()
                for i in range(0, minor_number):
                    min_fname = input("Enter the minor first name:\n ").title()
                    min_lname = input("Enter the minor last name:\n ").title()
                    min_p_number = input("Enter the minor passport number :\n ")
                    min_dob = input("Enter the minor date of birth as DD/MM/YYYY:\n ")
                    min_home_address = input("Enter the minor home address:\n ")
            elif choice_0_1_1 =="no":
                continue
            departure_date = input("What day do you wish to depart?\n Format is DD/MM/YYYY: ")
            
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

    # a booking and all its details can be changed
    elif choice_0_1 == 2:
        while True:
            print("""\nPick an option:
                    1. Change passenger information
                    2. Change flight details
                    3. EXIT""")

        # if the user inputs an invalid option the code runs again
        try:
            choice_0_1_2 = int(input("--->  "))
            try: 
                if choice_0_1_2 in range(1, 4):
                    continue
            except:
                continue
        except:
            continue
        
        # change passenger information, find out which information to change
        if choice_0_1_2 == 1:
            while True:
                print("""\nPick an option:
                        1. Change passport number
                        2. Change other passenger information
                        3. EXIT""")
            # if the user inputs an invalid option the code runs again
            try:
                choice_0_1_2_1= int(input("--->  "))
                try: 
                    if choice_0_1_2_1 in range(1, 4):
                        continue
                except:
                    continue
            except:
                continue
        # either the full name or the passport number remains the same
        # we use sql to extract all the data on the passenger and UPDATE the relevant column
        if choice_0_1_2_1 == 1:
            while True:
                print("\nIn order to change passenger passport number please answer the following questions: ")
                fname = input("Enter passenger first name:\n ").title()
                lname = input("Enter passenger last name:\n ").title()
                dob = input("Enter passenger date of birth as DD/MM/YYYY:\n ")
                # we use sql to extract all the data on the passenger and UPDATE the relevant column

        # change passemger personal information
        elif choice_0_1_2_1 == 2:
            while True:
                print("\nIn order to change passenger personal information please answer the following question: ")
                p_number = input("Enter passenger passport number:\n ")
                # we use sql to extract all the data on the passenger and UPDATE the relevant column

        # exit the interface
        elif choice_0_1_2_1 == 3:
                print("""\nEXIT""")
                break

 
        elif choice_0_1_2 == 2:
            while True:
                departure_date = input("What day do you wish to depart?\n Format is DD/MM/YYYY: ")
                
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
    
    # exit option was selected on the second menu
    elif choice_0_1 == 3:
        print("Thank you for your time, have a pleasant journey.")
        break
 
    if choice_0 == 2:
        while True:
            print("Welcome to the flight manager.")
            print("""\nPick an option:
                    1. Create a flight route
                    2. Change the details of an existing flight route
                    3. Cancel a route
                    4. EXIT""")
