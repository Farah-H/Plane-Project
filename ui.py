from user_guest import Guest
from user_admin import Admin
from user_staff import Staff


class Flight:
    def __init__(
        self,
        airline_id,
        airline_name,
        from_location,
        to_location,
        departure_time,
        arrival_time,
        flight_duration,
        total_seats,
    ):
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
    while True:
        print(
            """\nPick an option:
                1. View flights
                2. Login
                3. Exit"""
        )

        # if the user inputs an invalid option the code runs again
        try:
            choice_initial = int(input("---> "))
        except:
            print("Invalid input, please try again!")
        else:
            if choice_initial == 1:
                while True:
                    print(
                        """\nPick an option:
                            1. View all available flights
                            2. View all outbound flights for a selected destination
                            3. View all outbound flights for a selected date
                            4. View all outbound flights for a selected destination and date
                            5. Exit"""
                    )

                    # if the user inputs an invalid option the code runs again
                    try:
                        choice_view = int(input("---> "))
                    except:
                        continue
                    else:
                        if choice_view == 1:
                            guest = Guest()
                            print(guest.all_flights())

                        elif choice_view == 2:
                            destination_to_view = input(
                                "Please enter your destination\n"
                            )
                            guest = Guest()
                            flight_info = guest.display_flight(destination_to_view)
                            if flight_info != False:
                                print(flight_info)
                            else:
                                print("This destination is not available")

                        elif choice_view == 3:
                            date_to_view = input(
                                "Please enter your departure date as DDMMYYYY\n"
                            )

                        elif choice_view == 4:
                            destination_to_view = input(
                                "Please enter your destination\n"
                            )
                            date_to_view = input(
                                "Please enter your departure date as DDMMYYYY\n"
                            )

                        elif choice_view == 5:
                            break
                        else:
                            print("Pick 1, 2, 3 or 4")

            elif choice_initial == 2:
                can_login = False
                # prompt the user to enter login details to access the booking system
                print("Please login to continue")
                username = input("Username:\n")
                password = input("Password:\n")

                try:
                    user = Admin(username, password)
                    if user.permission_level != "admin":
                        raise Exception()
                except:
                    try:
                        user = Staff(username, password)
                        if user.permission_level != "user":
                            raise Exception()
                    except:
                        print("Login details incorrect, please try again!")
                    else:
                        can_login = True
                else:
                    can_login = True

                if can_login:
                    while True:
                        print(
                            """\nPick an option:
                                1. Passenger booking manager
                                2. Flight manager#
                                3. Admin Panel
                                4. EXIT"""
                        )

                        # if the user inputs an invalid option the code runs again
                        try:
                            choice_0 = int(input("--->  "))

                        except:
                            print("This is not a valid option. Please try again!")
                        else:
                            if choice_0 == 1:
                                while True:
                                    print("Welcome to the booking manager.")
                                    print(
                                        """\nPick an option:
                                                1. Make a booking
                                                2. Change the details of an existing booking
                                                3. Cancel a booking
                                                4. EXIT"""
                                    )

                                    # if the user inputs an invalid option the code runs again
                                    try:
                                        choice_0_1 = int(input("--->  "))
                                    except:
                                        print(
                                            "This is not a valid option. Please try again!"
                                        )
                                    else:
                                        # user is prompted to enter information required to make a booking
                                        if choice_0_1 == 1:
                                            while True:
                                                print(
                                                    "\nIn order to make a booking, please answer the following questions: "
                                                )
                                                fname = input(
                                                    "Enter passenger first name:\n "
                                                ).title()
                                                lname = input(
                                                    "Enter passenger last name:\n "
                                                ).title()
                                                p_number = input(
                                                    "Enter passenger passport number:\n "
                                                )
                                                dob = input(
                                                    "Enter passenger date of birth as DD/MM/YYYY:\n "
                                                )
                                                home_address = input(
                                                    "Enter passenger home address:\n "
                                                )
                                                email_address = input(
                                                    "Enter passenger email address:\n "
                                                )
                                                telephone = input(
                                                    "Enter passenger telephone number:\n "
                                                )

                                                # accompanied minor or minors will also need to input details
                                                choice_0_1_1 = input(
                                                    "YES or NO\nIs the passenger travelling with a minor? "
                                                ).lower()
                                                if choice_0_1_1 == "yes":
                                                    minor_number = input(
                                                        "How many minors are you travelling with:\n "
                                                    ).int()
                                                    for i in range(0, minor_number):
                                                        min_fname = input(
                                                            "Enter the minor first name:\n "
                                                        ).title()
                                                        min_lname = input(
                                                            "Enter the minor last name:\n "
                                                        ).title()
                                                        min_p_number = input(
                                                            "Enter the minor passport number :\n "
                                                        )
                                                        min_dob = input(
                                                            "Enter the minor date of birth as DD/MM/YYYY:\n "
                                                        )
                                                        min_home_address = input(
                                                            "Enter the minor home address:\n "
                                                        )
                                                elif choice_0_1_1 == "no":
                                                    continue
                                                departure_date = input(
                                                    "What day do you wish to depart?\n Format is DD/MM/YYYY: "
                                                )

                                                # list of cities and countries combined
                                                atlas = []

                                                # from_location existence is verified
                                                from_location = input(
                                                    "Where will you be travelling from?\n"
                                                )
                                                if from_location in atlas:
                                                    continue
                                                else:
                                                    print(
                                                        "Please enter a valid departure location."
                                                    )

                                                # from_location existence is verified
                                                to_location = input(
                                                    "Where will you be travelling to?\n"
                                                )
                                                if from_location in atlas:
                                                    continue
                                                else:
                                                    print(
                                                        "Please enter a valid destination location."
                                                    )

                                        # a booking and all its details can be changed
                                        elif choice_0_1 == 2:
                                            while True:
                                                print(
                                                    """\nPick an option:
                                                        1. Change passenger information
                                                        2. Change flight details
                                                        3. EXIT"""
                                                )

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
                                                    print(
                                                        """\nPick an option:
                                                            1. Change passport number
                                                            2. Change other passenger information
                                                            3. EXIT"""
                                                    )
                                                # if the user inputs an invalid option the code runs again
                                                try:
                                                    choice_0_1_2_1 = int(
                                                        input("--->  ")
                                                    )
                                                    try:
                                                        if choice_0_1_2_1 in range(
                                                            1, 4
                                                        ):
                                                            continue
                                                    except:
                                                        continue
                                                except:
                                                    continue
                                            # either the full name or the passport number remains the same
                                            # we use sql to extract all the data on the passenger and UPDATE the relevant column
                                            if choice_0_1_2_1 == 1:
                                                while True:
                                                    print(
                                                        "\nIn order to change passenger passport number please answer the following questions: "
                                                    )
                                                    fname = input(
                                                        "Enter passenger first name:\n "
                                                    ).title()
                                                    lname = input(
                                                        "Enter passenger last name:\n "
                                                    ).title()
                                                    dob = input(
                                                        "Enter passenger date of birth as DD/MM/YYYY:\n "
                                                    )
                                                    # we use sql to extract all the data on the passenger and UPDATE the relevant column

                                                # change passemger personal information
                                            elif choice_0_1_2_1 == 2:
                                                while True:
                                                    print(
                                                        "\nIn order to change passenger personal information please answer the following question: "
                                                    )
                                                    p_number = input(
                                                        "Enter passenger passport number:\n "
                                                    )
                                                    # we use sql to extract all the data on the passenger and UPDATE the relevant column

                                            # exit the interface
                                            elif choice_0_1_2_1 == 3:
                                                print("""\nEXIT""")
                                                break

                                            elif choice_0_1_2 == 2:
                                                while True:
                                                    departure_date = input(
                                                        "What day do you wish to depart?\n Format is DD/MM/YYYY: "
                                                    )

                                                    # from_location existence is verified
                                                    from_location = input(
                                                        "Where will you be travelling from?\n"
                                                    )
                                                    if from_location in atlas:
                                                        continue
                                                    else:
                                                        print(
                                                            "Please enter a valid departure location."
                                                        )

                                                    # from_location existence is verified
                                                    to_location = input(
                                                        "Where will you be travelling to?\n"
                                                    )
                                                    if from_location in atlas:
                                                        continue
                                                    else:
                                                        print(
                                                            "Please enter a valid destination location."
                                                        )

                                            # exit option was selected on the second menu
                                            elif choice_0_1 == 3:
                                                print(
                                                    "Thank you for your time, have a pleasant journey."
                                                )
                                                break

                                            if choice_0 == 2:
                                                while True:
                                                    print(
                                                        "Welcome to the flight manager."
                                                    )
                                                    print(
                                                        """\nPick an option:
                                                            1. Create a flight route
                                                            2. Change the details of an existing flight route
                                                            3. Cancel a route
                                                            4. EXIT"""
                                                    )

                                        else:
                                            if choice_initial not in range(1, 3):
                                                print("Pick 1 or 2")
                            elif choice_0 == 3:
                                print("Who would you like to view?")
                                user_choice = input("=> ")
                                if user_choice != False:
                                    print(user.view_user(user_choice))
                                else:
                                    print("This user does not exist")
                            elif choice_0 == 4:
                                break
                            else:
                                print("Thats not a valid choice")
            elif choice_initial == 3:
                break
            else:
                print("This is not a valid option")


if __name__ == "__main__":
    body()