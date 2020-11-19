import os
import getpass
import time
import random
from datetime import datetime
from user_guest import Guest
from user_staff import Staff
from user_admin import Admin


def personal_information(adult_count, teen_count, children_count):
    final_output = []
    while True:
        print("We need some information about the main passenger.")

        passport = input("Passport Number: ")
        fname = input("First Name: ")
        lname = input("Last Name: ")
        print("Date of birth. Format: YYYY MM DD")
        dob = input("=> ").split(" ")
        if len(dob) == 3:
            try:
                dob = "-".join(dob)
            except:
                print("Invalid date of birth!\nPlease try again")
            else:
                print(
                    f"{fname} {lname}.\nPassport Number: {passport}.\nDate of birth: {dob}\nIs that correct?"
                )
                correct = input("=> ")
                if correct == "yes":
                    final_output.append(
                        [
                            passport,
                            fname,
                            lname,
                            dob,
                            f"F{random.randint(100, 999)}",
                            "NULL",
                        ]
                    )
                    main_pass = True
        else:
            print("Invalid date of birth provided!\nPlease try again")
            return False

        if main_pass:
            count = 0
            while count < sum(adult_count, teen_count, children_count):
                print("We need some information about the other passengers.")

                passport = input("Passport Number: ")
                fname = input("First Name: ")
                lname = input("Last Name: ")
                print("Date of birth. Format: YYYY MM DD")
                dob = input("=> ").split(" ")
                if len(dob) == 3:
                    try:
                        dob = "-".join(dob)
                    except:
                        print("Invalid date of birth!\nPlease try again")
                    else:
                        print(
                            f"{fname} {lname}.\nPassport Number: {passport}.\nDate of birth: {dob}\nIs that correct?"
                        )
                        correct = input("=> ")
                        if correct == "yes":
                            final_output.append(
                                [
                                    passport,
                                    fname,
                                    lname,
                                    dob,
                                    final_output[0][0],
                                    f"F{random.randint(100, 999)}",
                                ]
                            )
                else:
                    print("Invalid date of birth provided!\nPlease try again")
                    return False


def booking_loop(user, data, amount):
    clear()
    while True:
        print("-= Ticket Information =-=")

        if amount > 1:
            print(
                "Are you travelling with children under the age of 13?\nInput the amount of children or use '0' for none."
            )

            try:
                children = int(input("=> "))
            except:
                print("Please input a valid integer number")
            else:
                temp_amount = amount - children

                if temp_amount > 0:
                    print(
                        "Are you travelling with any teens aged 13-18?\nInput the amount of teenagers or use '0' for none."
                    )

                    try:
                        teens = int(input("=> "))
                    except:
                        print("Please input a valid integer number")
                    else:
                        final_amount = temp_amount - teens
                        output = []
                        if final_amount != 0:
                            adults = final_amount
                            teenagers = teens
                            child = children
                            output = personal_information(adults, teenagers, child)
                            if output == False:
                                print(
                                    "You've provided incorrect information.\nPlease try booking again!"
                                )
                                break
                            else:
                                output.insert(0, "NULL")
                                output.insert(0, datetime.now())
                                output.insert(0, "British Airways")
                                output.insert(0, user.staff_id)
                                output.insert(0, data[0])
                                price = 0
                                if adults > 0:
                                    price = price + (100 * adults)
                                if teenagers > 0:
                                    price = price + (80 * teenagers)
                                if child > 0:
                                    price = price + (60 * child)

                                output.insert(-1, price)
                        else:
                            adults = 0
                            teenagers = teens
                            child = children
                            output = personal_information(adults, teenagers, child)
                            if output == False:
                                print(
                                    "You've provided incorrect information.\nPlease try booking again!"
                                )
                                break
                            else:
                                output.insert(0, "NULL")
                                output.insert(0, datetime.now())
                                output.insert(0, "British Airways")
                                output.insert(0, user.staff_id)
                                output.insert(0, data[0])
                                price = 100
                                if teenagers > 0:
                                    price = price + (80 * teenagers)
                                if child > 0:
                                    price = price + (60 * child)

                                output.insert(-1, price)

                        for ticket in output:
                            if isinstance(ticket, list):
                                user.add_passengers(
                                    output[0],
                                    output[1],
                                    output[2],
                                    output[3],
                                    output[4],
                                    ticket,
                                    output[-1],
                                )

                        print(
                            f"Total ticket price: {output[-1]}.\nThank you for using our services!"
                        )
                        break

        else:
            print("We need your personal information to complete the booking.")

            passport = input("Passport Number: ")
            fname = input("First Name: ")
            lname = input("Last Name: ")
            print("Date of birth. Format: YYYY MM DD")
            dob = input("=> ").split(" ")
            if len(dob) == 3:
                try:
                    dob = "-".join(dob)
                except:
                    print("Invalid date of birth!\nPlease try again")
                else:
                    print(
                        f"{fname} {lname}.\nPassport Number: {passport}.\nDate of birth: {dob}\nIs that correct?"
                    )
                    correct = input("=> ")
                    if correct == "yes":
                        output = [
                            passport,
                            fname,
                            lname,
                            dob,
                            f"F{random.randint(100, 999)}",
                        ]
                        output.insert(0, "NULL")
                        output.insert(0, datetime.now())
                        output.insert(0, "British Airways")
                        output.insert(0, user.staff_id)
                        output.insert(0, data[0])
                        output.insert(-1, 100)

                        user.add_single_passenger(output)
                        print(
                            f"Total ticket price: £100.\nThank you for using our services!"
                        )
                        break
            else:
                print("Invalid date of birth provided!\nPlease try again")
                return False

        time.sleep(3)
        clear()


def booking(user):
    clear()
    while True:
        print("-= Booking System =-")
        print("What flight would you like to book? (or say 'exit')\n")
        flight_ref = input("=> ")
        if flight_ref != "exit":
            if flight_ref.isdigit():
                flight_ref = int(flight_ref)
                try:
                    flight_data = user.display_flight_id(flight_ref)
                except Exception as e:
                    print(e)
                    print("There was an issue with database. Please try again later!")
                else:
                    if flight_data != False:
                        print(f"Available seat number: {flight_data[0][7]}")
                        if flight_data[0][7] > 0:
                            while True:
                                print(
                                    "How many tickets would you like to book including yourself? (or say 'exit')"
                                )

                                ticket_amount = input("=> ")
                                if ticket_amount != "exit":
                                    if ticket_amount.isdigit():
                                        ticket_amount = int(ticket_amount)
                                        if flight_data[0][7] >= ticket_amount:
                                            booking_loop(
                                                user, flight_data[0], ticket_amount
                                            )
                                        else:
                                            print(
                                                "We do not have that many seats available."
                                            )
                                    else:
                                        print("Please input an integer number!")
                                else:
                                    break
                        else:
                            print("There is not enough seats available.")
                    else:
                        print("This flight doesn't exist!")
            else:
                print("Please input an integer number!")
        else:
            break
        time.sleep(3)
        clear()


def check_each_passenger(user, data):
    clear()
    while True:
        print(
            """
        -= Passenger Check =-
    Please input each passanger information one at a time.
        """
        )

        fname = input("First Name: ")
        lname = input("Last Name: ")
        passport = input("Passport Number: ")
        print("Date of birth. Format: YYYY MM DD")
        dob = input("=> ").split(" ")

        try:
            dob = "-".join([int(a) for a in dob])
        except:
            print("Please input correct date format")
        else:
            while True:
                print(
                    f"{fname} {lname}.\nPassport number: {passport}.\nDate of birth: {dob}"
                )
                print("Is that correct?")
                correct = input("=> ")

                if correct == "yes":
                    match = False
                    for passenger in data:
                        if (
                            fname in passenger
                            and lname in passenger
                            and passport in passenger
                            and dob in passenger
                        ):
                            match = True
                            break
                    if match:
                        print("Passenger information is correct.")
                    else:
                        print("Passenger information is incorrect")
                    break
                elif correct == "no":
                    print("Please input the information again.")
                    break
                else:
                    print("Please input 'yes' or 'no'.")

        more = True
        while True:
            print("Would you like to check another?")
            choice = input("=> ")
            if choice == "yes":
                break
            elif choice == "no":
                more = False
                break
            else:
                print("Please input 'yes' or 'no'.")
        if not more:
            break
        time.sleep(3)
        clear()


def security_check(user):
    clear()
    while True:
        print(
            f"""
        -= Security Check =-
    Please provide the flight number

    """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            try:
                data = user.security_check(choice)
            except:
                print("There was an issue with the database. Please try again later")
            else:
                if data != False:
                    while True:
                        print(
                            "Would you like to see all the data before checking each passenger?"
                        )
                        user_input = input("=> ")
                        if user_input == "yes":
                            ## NEEDS FORMATTING
                            print(data)
                            time.sleep(5)
                            check_each_passenger(user, data)
                            break
                        elif user_input == "no":
                            check_each_passenger(user, data)
                            break
                        else:
                            print("Please input 'yes' or 'no'.")
                else:
                    print("There is no flight with this reference number.")
        else:
            print("Please input an integer number!")
        time.sleep(3)
        clear()


def passanger_management(user):
    clear()
    while True:
        print(
            f"""
        -= Passanger Management =-
    Select one of the options

    1. View passenger information
    2. Edit passenger information
    3. Remove passanger from a flight
    4. Go Back
        """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                while True:
                    print("Please provide the first and last name of the passenger.")
                    fname = input("First Name: ")
                    lname = input("Last Name: ")

                    if fname.isalpha() and lname.isalpha():
                        print(f"{fname} {lname}, is that correct?")
                        confirm = input("=> ")
                        if confirm == "yes":
                            try:
                                data = user.display_passenger(fname, lname)
                            except:
                                print(
                                    "There was an issue with the database. Please try again later."
                                )
                            else:
                                if data != False:
                                    ## NEEDS FORMATTING
                                    print(data)
                                    break
                                else:
                                    print("Passenger was not found!")
                        elif confirm == "no":
                            pass
                        else:
                            print("Please input a 'yes' or 'no' answer.")
                    else:
                        print(
                            "Please only input alphabetical characters for first and last name."
                        )
            elif choice == 2:
                while True:
                    print(
                        "Please input the following information to edit the passenger."
                    )

                    passport = input("Passport number: ")
                    column = input("Column to change: ")
                    new_info = input("New information: ")

                    print(
                        f"Passport number {passport}, changing {column} information.\nNew information: {new_info}"
                    )
                    print("Is that correct?")
                    confirm = input("=> ")
                    if confirm == "yes":
                        try:
                            user.change_passenger(passport, column, new_info)
                        except:
                            print("Passport number not found")
                        else:
                            break
                    elif confirm == "no":
                        pass
                    else:
                        print("Please input a 'yes' or 'no' answer.")
            elif choice == 3:
                pass
            elif choice == 4:
                clear()
                break
            else:
                print("That's not a valid option\nPlease try again")
        else:
            print("Please input an integer number!")
        time.sleep(3)
        clear()


def account_settings(user):
    clear()
    while True:
        print(
            f"""
        -= Account Settings =-
    Select one of the options

    1. Change account information
    2. Change password
    3. Go back
        """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                clear()
                break
            else:
                print("That's not a valid option\nPlease try again")
        else:
            print("Please input an integer number!")
        time.sleep(3)
        clear()


def staff_menu(user):
    clear()
    while True:
        print(
            f"""
        -= Staff Menu =-
    Select one of the options

    1. Book a flight
    2. Passenger Management
    3. Display flight information
    4. Check available seats
    5. Security Check
    6. Account settings
    7. {"Log out" if user.permission_level == "user" else "Go Back"}
        """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                booking(user)
            elif choice == 2:
                passanger_management(user)
            elif choice == 3:
                print(
                    """
    How would you like to look up a flight?

    1. Flight ID
    2. Flight Destination
    3. Flight Date
    """
                )
                user_input = input("=> ")
                if user_input.isdigit():
                    user_input = int(user_input)

                    if user_input == 1:
                        print("Please input the Flight ID")
                        flight_id = input("=> ")
                        if flight_id.isdigit():
                            flight_id = int(flight_id)
                            try:
                                data = user.display_flight_id(flight_id)
                            except:
                                print(
                                    "There was an issue with the Database.\nPlease try again later"
                                )
                            else:
                                if data != False:
                                    ## NEEDS FORMATING
                                    print(data)
                                else:
                                    print("This Flight ID doesn't exist")
                        else:
                            print("Please input an integer number!")
                    elif user_input == 2:
                        print("Please input the Flight Destination")
                        flight_destination = input("=> ")
                        try:
                            data = user.display_flight_destination(flight_destination)
                        except:
                            print(
                                "There was an issue with the Database.\nPlease try again later"
                            )
                        else:
                            if data != False:
                                ## NEEDS FORMATING
                                print(data)
                            else:
                                print("This Flight Destination doesn't exist")

                    elif user_input == 3:
                        print("Please input the Flight Date. Format: YYYY MM DD")
                        departure = input("=> ").split(" ")
                        if len(departure) == 3:
                            try:
                                departure = datetime(
                                    int(departure[0]),
                                    int(departure[1]),
                                    int(departure[2]),
                                )
                            except:
                                print(
                                    "Thats not a correct date format!\nPlease try again"
                                )
                            else:
                                try:
                                    data = user.display_flight_date(departure)
                                except:
                                    print(
                                        "There was an issue with the Database.\nPlease try again later"
                                    )
                                else:
                                    if data != False:
                                        ## FORMATTING NEEDED
                                        print(data)
                                    else:
                                        print("This flight date doesn't exist")
                        else:
                            print("Please use the correct format YYYY MM DD")
                    else:
                        print("That's not a valid option\nPlease try again")

                else:
                    print("Please input an integer number!")
            elif choice == 4:
                print("Please input the Flight ID")
                flight_id = input("=> ")
                if flight_id.isdigit():
                    flight_id = int(flight_id)
                    try:
                        data = user.display_flight_id(flight_id)
                    except:
                        print(
                            "There was an issue with the Database.\nPlease try again later"
                        )
                    else:
                        if data != False:
                            print(
                                f"Available seats for flight ID {flight_id}: {data[8]}"
                            )
                        else:
                            print("This Flight ID doesn't exist")
                else:
                    print("Please input an integer number!")
            elif choice == 5:
                security_check(user)
            elif choice == 6:
                account_settings(user)
            elif choice == 7:
                clear()
                break
            else:
                print("That's not a valid option\nPlease try again")

        else:
            print("Please input an integer number!")
        time.sleep(3)
        clear()


def user_management(user):
    clear()
    while True:
        print(
            """
        -= User Management =-
    Select one of the options

    1. Add a new user
    2. Remove a user
    3. Edit user permissions
    4. View user information
    5. Go back
        """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print("Please provide a username and password for the new user.")
                username = input("Username: ")
                password = getpass.getpass("Password: ")

                try:
                    user.add_staff(username, password)
                except:
                    print("Username already exists")

            elif choice == 2:
                print("Please provide the username that you would like to remove.")
                username = input("Username: ")

                try:
                    user.remove_staff(username)
                except:
                    print("Username not found.")

            elif choice == 3:
                print("Please provide a username and new permission to be set.")

                username = input("Username: ")
                permissions = input("Permissions: ")

                if (
                    permissions == "admin"
                    or permissions == "user"
                    or permissions == "guest"
                ):
                    try:
                        user.change_permissions(username, permissions)
                    except:
                        print("Uesrname not found.")
                else:
                    print("Incorrect permission name.")

            elif choice == 4:
                print("Please provide the username that you would like to view.")
                username = input("Username: ")

                try:
                    data = user.view_user(username)
                except:
                    print("Username not found.")
                else:
                    ## NEEDS FORMATTING
                    print(data)
            elif choice == 5:
                clear()
                break
            else:
                print("That's not a valid option\nPlease try again")
        else:
            print("Please input an integer number!")
        time.sleep(3)
        clear()


def flight_management(user):
    clear()
    while True:
        print(
            """
        -= Flight Management =-
    Select one of the options

    1. Add a new flight
    2. Remove a flight
    3. Edit a flight
    4. Go back
            """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print("Please input the following information:")
                details = {}
                journey_columns = [
                    "plane_id",
                    "departure_time",
                    "arrival_time",
                    "departing_from",
                    "arriving_to",
                ]
                for option in journey_columns:
                    display = option
                    while True:
                        user_input = input(
                            f"{str(display).replace('_', ' ').title()}: "
                        )
                        if user_input.isalpha():
                            details[option] = user_input
                            break
                        elif user_input.isdigit():
                            details[option] = int(user_input)
                            break
                        else:
                            print("Not a valid input. Please try again")
                try:
                    user.add_flight(details)
                except:
                    print(
                        "Failed to add the plane.\nCheck that your details are correct and try again."
                    )
            elif choice == 2:
                print("Please input a flight ID number.")
                user_input = input("=> ")
                if user_input.isdigit():
                    try:
                        user.remove_flight(user_input)
                    except:
                        print("This flight doesn't exist.")
                else:
                    print("Please input an integer number")
            elif choice == 3:
                print("Please input the information needed to perform an edit.")

                flight_ref = input("Flight ID: ")
                column = input("Column name: ")
                new_info = input("New information: ")

                if flight_ref.isdigit():
                    try:
                        user.edit_flight(flight_ref, column, new_info)
                    except:
                        print("This flight doesn't exist or wrong data was provided.")
                else:
                    print("Please input an integer number for Flight ID")

            elif choice == 4:
                clear()
                break
            else:
                print("That's not a valid option\nPlease try again")

        else:
            print("Please input an integer number!")
        time.sleep(3)
        clear()


def plane_management(user):
    clear()
    while True:
        print(
            """
        -= Plane Management =-
    Select one of the options

    1. Add a new plane
    2. Remove a plane
    3. Edit a plane
    4. Go back
            """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print("Please input the following information:")
                details = {}
                plane_columns = [
                    "plane_type",
                    "plane_capacity",
                    "plane_size",
                    "fuel_capacity",
                    "speed",
                    "weight",
                    "seats_available",
                    "fuel_per_km",
                    "maintenance_date",
                ]
                for option in plane_columns:
                    display = option
                    while True:
                        user_input = input(
                            f"{str(display).replace('_', ' ').title()}: "
                        )
                        if user_input.isalpha() or option == "maintenance_date":
                            details[option] = user_input
                            break
                        elif user_input.isdigit():
                            details[option] = int(user_input)
                            break
                        else:
                            print("Not a valid input. Please try again")
                try:
                    user.add_plane(details)
                except:
                    print(
                        "Failed to add the plane.\nCheck that your details are correct and try again."
                    )

            elif choice == 2:
                print("Please input a plane ID number.")
                user_input = input("=> ")
                if user_input.isdigit():
                    try:
                        user.remove_plane(user_input)
                    except:
                        print("This plane doesn't exist.")
                else:
                    print("Please input an integer number")
            elif choice == 3:
                print("Please input the information needed to perform an edit.")

                plane_ref = input("Plane ID: ")
                column = input("Column name: ")
                new_info = input("New information: ")

                if plane_ref.isdigit():
                    try:
                        user.edit_flight(plane_ref, column, new_info)
                    except:
                        print("This plane doesn't exist or wrong data was provided.")
                else:
                    print("Please input an integer number for Plane ID")
            elif choice == 4:
                clear()
                break
            else:
                print("That's not a valid option\nPlease try again")

        else:
            print("Please input an integer number!")
        time.sleep(3)
        clear()


def admin_menu(user):
    clear()
    while True:
        print(
            """
        -= Administrator Menu =-
    Select one of the options

    1. Staff Management
    2. Flight Management
    3. Plane Management
    4. Backup System
    5. Staff Actions
    6. Log out
        """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)

            if choice == 1:
                user_management(user)
            elif choice == 2:
                flight_management(user)
            elif choice == 3:
                plane_management(user)
            elif choice == 4:
                print("Please input the table you would like to back up and file name.")
                print("Acceptable format: '.json'")

                table_name = input("Table name: ")
                file_name = input("File name: ")

                if ".json" in file_name:
                    try:
                        old_data = user.backup_table(table_name, file_name)
                    except:
                        print("This table name doesn't exist.")
                    else:
                        while True:
                            print("Would you like to view old data? (yes/no)")
                            data_choice = input("=> ")
                            if data_choice == "yes":
                                ## NEEDS FORMATTING
                                print(old_data)
                                break
                            elif data_choice == "no":
                                break
                            else:
                                print("Incorrect input. Please write 'yes' or 'no'.")
                else:
                    print("Unsuppored file format")

            elif choice == 5:
                staff_menu(user)
            elif choice == 6:
                clear()
                break
            else:
                print("That's not a valid option\nPlease try again")

        else:
            print("Please input an integer number!")
        time.sleep(3)
        clear()


def login_menu():
    clear()
    while True:
        print(
            """
        -= Login =-
    Please input your login details
        """
        )
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        try:
            user = Staff(username, password)
            if user.permission_level == "admin":
                user = Admin(username, password)
        except:
            print("Login information incorrect!\nPlease try again.")
            time.sleep(5)
        else:
            if user.permission_level == "user":
                staff_menu(user)
            elif user.permission_level == "admin":
                admin_menu(user)
            else:
                print("Permission Error. Please try again!")
                time.sleep(3)
                clear()
                break
            clear()
            break


def guest_menu():
    clear()
    user = Guest()
    while True:
        print(
            """
        -= Guest Menu =-
    See all the flights!

    1. View next 10 flights
    2. View flights to a specific destination
    3. View flights on a specific date
    4. Go Back
        """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                data = user.all_flights()
                if data != False:
                    ## FORMATTING NEEDED
                    print(data)
                else:
                    print(
                        "We had an issue retriving flight data.\nPlease try again later."
                    )

            elif choice == 2:
                print("What destination are you interested in?")
                destination = input("=> ")
                data = user.display_flight_destination(destination)
                if data != False:
                    ## FORMATTING NEEDED
                    print(data)
                else:
                    print("That's not a valid destination.\nPlease try again")

            elif choice == 3:
                print("What day would you like to fly?\nFormat: YYYY MM DD")
                departure = input("=> ").split(" ")
                if len(departure) == 3:
                    try:
                        departure = datetime(
                            int(departure[0]), int(departure[1]), int(departure[2])
                        )
                    except:
                        print("Thats not a correct date format!\nPlease try again")
                    else:
                        data = user.display_flight_date(departure)
                        if data != False:
                            ## FORMATTING NEEDED
                            print(data)
                        else:
                            print("That's not a valid date.\nPlease try again")
                else:
                    print("Please use the correct format YYYY MM DD")

            elif choice == 4:
                user = None
                clear()
                break
            else:
                print("That's not a valid choice.\nPlease try again")
        else:
            print("Please input an integer number.")
        time.sleep(3)
        clear()


def main():
    clear()
    while True:
        print(
            """
        -= London Heathrow Airport =-
    Select one of the Options

    1. Guest Menu
    2. Login
    3. Exit
    """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)

            if choice == 1:
                guest_menu()
            elif choice == 2:
                login_menu()
            elif choice == 3:
                clear()
                break
            else:
                print("That's not a valid option\nPlease try again")

        else:
            print("Please input an integer number!")
        time.sleep(3)
        clear()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()