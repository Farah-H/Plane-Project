import os
import getpass
import time
import random
import math
import datetime
from prettytable import PrettyTable
from user_guest import Guest
from user_staff import Staff
from user_admin import Admin


def calculate_age(age):
    born = datetime.datetime.strptime(age, "%Y-%m-%d")
    today = datetime.date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age


def calculate_price(age):
    age = calculate_age(age)
    if age < 18 and age > 13:
        return 80
    elif age < 13:
        return 60
    else:
        return 100


def booking(user):
    clear()
    while True:
        text = ["-= Booking System =-", "Which flight would you like to book?"]
        prompt(text)
        flight_ref = input("=> ")
        if flight_ref.isdigit():
            flight_ref = int(flight_ref)

            flight_exists = user.display_flight_id(flight_ref)
            if flight_exists != False:
                text = ["How many tickets would you like to book?"]
                prompt(text)
                amount = input("=> ")
                if amount.isdigit():
                    amount = int(amount)
                    count = 0
                    ticket_data = []
                    while count < amount:
                        text = ["Please input all your passport information."]
                        prompt(text)

                        passport_id = input("Passport Number: ")
                        text = ["Format: YYYY MM DD"]
                        prompt(text)
                        issue_date = input("Issue Date: ").split(" ")

                        if len(issue_date) == 3:
                            issue_date = "-".join(issue_date)

                            text = ["Format: YYYY MM DD"]
                            prompt(text)
                            expiry_date = input("Expiry Date: ").split(" ")

                            if len(expiry_date) == 3:
                                expiry_date = "-".join(expiry_date)
                                expired = 0
                                text = ["What is the country code of your passport?"]
                                prompt(text)
                                country_code = input("=> ")

                                text = [
                                    "Please confirm your infromation",
                                    f"Passport Number: {passport_id}",
                                    f"Issue Date: {issue_date}",
                                    f"Expiry Date: {expiry_date}",
                                    f"Country Code: {country_code}",
                                ]
                                prompt(text)
                                choice = input("Is that correct?\n=> ")

                                if choice == "yes":
                                    try:
                                        user.add_passport(
                                            passport_id,
                                            issue_date,
                                            expiry_date,
                                            expired,
                                            country_code,
                                        )
                                    except:
                                        text = [
                                            "Unable to insert the passport.",
                                            "Please try again",
                                        ]
                                        prompt(text)
                                    else:
                                        text = [
                                            "Please input all your personal information."
                                        ]
                                        prompt(text)

                                        fname = input("First Name: ")
                                        lname = input("Last Name: ")
                                        text = ["Format: YYYY MM DD"]
                                        prompt(text)
                                        dob = input("Date of birth: ").split(" ")

                                        if len(dob) == 3:
                                            dob = "-".join(dob)

                                            text = [
                                                "Please confirm your infromation",
                                                f"First Name: {fname}",
                                                f"Last Name: {lname}",
                                                f"Date of Birth: {dob}",
                                            ]
                                            prompt(text)
                                            choice = input("Is that correct?\n=> ")

                                            if choice.lower() == "yes":
                                                age = calculate_age(dob)

                                                if age > 18:
                                                    dependent = "NULL"
                                                    try:
                                                        passenger_id = (
                                                            user.add_passenger(
                                                                passport_id,
                                                                fname,
                                                                lname,
                                                                dob,
                                                                dependent,
                                                            )
                                                        )
                                                    except:
                                                        text = [
                                                            "Please input all your personal information."
                                                        ]
                                                        prompt(text)
                                                    else:
                                                        price = calculate_price(dob)
                                                        info = [
                                                            f"F{random.randint(100,999)}",
                                                            passenger_id,
                                                            price,
                                                        ]
                                                        ticket_data.append(info)
                                                        count += 1
                                                else:
                                                    dependent = ticket_data[0][1]
                                                    try:
                                                        passenger_id = (
                                                            user.add_passenger(
                                                                passport_id,
                                                                fname,
                                                                lname,
                                                                dob,
                                                                dependent,
                                                            )
                                                        )
                                                    except:
                                                        text = [
                                                            "Please input all your personal information."
                                                        ]
                                                        prompt(text)
                                                    else:
                                                        price = calculate_price(dob)
                                                        info = [
                                                            f"F{random.randint(100,999)}",
                                                            passenger_id,
                                                            price,
                                                        ]
                                                        ticket_data.append(info)
                                                        count += 1
                                            else:
                                                text = ["Please input the data again."]
                                                prompt(text)

                                        else:
                                            text = [
                                                "Please use the correct date format"
                                            ]
                                            prompt(text)

                                else:
                                    text = ["Please input the data again."]
                                    prompt(text)

                            else:
                                text = ["Please use the correct date format"]
                                prompt(text)

                        else:
                            text = ["Please use the correct date format"]
                            prompt(text)

                    date = datetime.datetime.now()
                    today = datetime.datetime.strptime(
                        f"{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}",
                        "%Y-%m-%d %H:%M",
                    )

                    price_total = 0
                    for i in range(len(ticket_data)):
                        if isinstance(ticket_data[i], list):
                            price_total += ticket_data[i][-1]

                    booking_id = user.add_booking(
                        today, user.staff_id, "British Airways", price_total
                    )

                    for i in range(len(ticket_data)):
                        if isinstance(ticket_data[i], list):
                            user.add_ticket(
                                flight_ref,
                                ticket_data[i][0],
                                1,
                                ticket_data[i][1],
                                booking_id,
                            )

                    text = [
                        f"The total for the booking is £{price_total}",
                        f"Your booking number is {booking_id}"
                        "Thank you for using our services!",
                        "We hope you enjoy your flight!",
                    ]
                    prompt(text)
                    break
                else:
                    text = ["Please input an integer number!"]
                    prompt(text)
            else:
                text = ["This flight number doesn't exist!", "Please try again"]
                prompt(text)

        else:
            text = ["Please input an integer number!"]
            prompt(text)


def check_each_passenger(user, data):
    while True:
        text = [
            "-= Passenger Check =-",
            "Please input each passanger information one at a time.",
        ]
        prompt(text)

        fname = input("First Name: ")
        lname = input("Last Name: ")
        passport = input("Passport Number: ")
        text = ["Date of birth.", "Format: YYYY MM DD"]
        prompt(text)
        birth = input("=> ").split(" ")

        try:
            dob = datetime.date(int(birth[0]), int(birth[1]), int(birth[2]))
        except:
            text = ["Please input correct date format"]
            prompt(text)
        else:
            while True:
                text = [
                    f"{fname} {lname}.",
                    f"Passport number: {passport}.",
                    f"Date of birth: {'-'.join(birth)}",
                    "Is that correct?",
                ]
                prompt(text)
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
                        text = [
                            "Passenger information is correct.",
                            "Enjoy your flight!",
                        ]
                        prompt(text)
                    else:
                        text = ["Passenger information is incorrect"]
                        prompt(text)
                    break
                elif correct == "no":
                    text = ["Please input the information again."]
                    prompt(text)
                    break
                else:
                    text = ["Please input 'yes' or 'no'."]
                    prompt(text)

        more = True
        while True:
            text = ["Would you like to check another?"]
            prompt(text)
            choice = input("=> ")
            if choice == "yes":
                clear()
                break
            elif choice == "no":
                more = False
                break
            else:
                text = ["Please input 'yes' or 'no'."]
                prompt(text)
        if not more:
            return True


def security_check(user):
    clear()
    action = False
    while True:
        text = ["-= Security Check =-", "Please provide the flight number"]
        prompt(text)
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            try:
                data = user.security_check(choice)
            except:
                text = [
                    "There was an issue with the database.",
                    "Please try again later",
                ]
                prompt(text)
            else:
                if data != False:
                    while True:
                        text = [
                            "Would you like to see all the data before checking each passenger?"
                        ]
                        prompt(text)
                        user_input = input("=> ")
                        if user_input == "yes":
                            security_columns = [
                                "First Name",
                                "Last Name",
                                "Date of Birth",
                                "Passport Number",
                            ]
                            table_printer(data, security_columns)
                            action = check_each_passenger(user, data)
                            break
                        elif user_input == "no":
                            action = check_each_passenger(user, data)
                            break
                        else:
                            text = ["Please input 'yes' or 'no'."]
                            prompt(text)
                else:
                    text = ["There is no flight with this reference number."]
                    prompt(text)
        else:
            text = ["Please input an integer number!"]
            prompt(text)

        if action:
            break


def passanger_management(user):
    clear()
    while True:
        text = [
            "-= Passanger Management =-",
            "Select one of the options",
            "",
            "1. View passenger information",
            "2. Edit passenger information",
            "3. Go Back",
        ]
        prompt(text)
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                while True:
                    text = ["Please provide the first and last name of the passenger."]
                    prompt(text)
                    fname = input("First Name: ")
                    lname = input("Last Name: ")

                    if fname.isalpha() and lname.isalpha():
                        text = [f"{fname} {lname}, is that correct?"]
                        prompt(text)
                        confirm = input("=> ")
                        if confirm == "yes":
                            try:
                                data = user.display_passenger(fname, lname)
                            except:
                                text = [
                                    "There was an issue with the database",
                                    "Please try again later.",
                                ]
                                prompt(text)
                            else:
                                if data != False:
                                    passenger_columns = [
                                        "First Name",
                                        "Last Name",
                                        "Date of Birth",
                                        "Passport Number",
                                        "Dependant On",
                                    ]

                                    table_printer(data, passenger_columns)
                                    break
                                else:
                                    text = ["Passenger was not found!"]
                                    prompt(text)
                        elif confirm != "no":
                            text = ["Please input a 'yes' or 'no' answer."]
                            prompt(text)

                    else:
                        text = [
                            "Please only input alphabetical characters for first and last name."
                        ]
                        prompt(text)
            elif choice == 2:
                while True:
                    text = [
                        "Please input the following information to edit the passenger."
                    ]
                    prompt(text)

                    passport = input("Passport number: ")
                    column = input("Column to change: ")
                    new_info = input("New information: ")

                    text = [
                        f"Passport number {passport},",
                        f"changing '{column}' information.",
                        f"New information: {new_info}",
                        "Is that correct?",
                    ]
                    prompt(text)
                    confirm = input("=> ")
                    if confirm == "yes":
                        try:
                            user.change_passenger(passport, column, new_info)
                        except:
                            text = ["Passport number not found"]
                            prompt(text)
                        else:
                            break
                    elif confirm != "no":
                        text = ["Please input a 'yes' or 'no' answer."]
                        prompt(text)

            elif choice == 3:
                clear()
                break
            else:
                text = ["That's not a valid option", "Please try again"]
                prompt(text)
        else:
            text = ["Please input an integer number!"]
            prompt(text)


def staff_menu(user):
    clear()
    while True:
        text = [
            "-= Staff Menu =-",
            " Select one of the options",
            "",
            "1. Book a flight",
            "2. Passenger Management",
            "3. Display flight information",
            "4. Check available seats",
            "5. Security Check",
            f'6. {"Log out" if user.permission_level == "user" else "Go Back"}',
        ]
        prompt(text)
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                booking(user)
            elif choice == 2:
                passanger_management(user)
            elif choice == 3:
                flight_columns = [
                    "Plane Type",
                    "Departure Time",
                    "Arrival Time",
                    "Departing From",
                    "Arriving To",
                    "Capacity",
                    "Seats Available",
                    "Country",
                    "Restrictions",
                    "Visa",
                ]
                text = [
                    "How would you like to look up a flight?",
                    "",
                    "1. Flight ID",
                    "2. Flight Destination",
                    "3. Flight Date",
                ]
                prompt(text)
                user_input = input("=> ")
                if user_input.isdigit():
                    user_input = int(user_input)

                    if user_input == 1:
                        text = ["Please input the Flight ID"]
                        prompt(text)
                        flight_id = input("=> ")
                        if flight_id.isdigit():
                            flight_id = int(flight_id)
                            try:
                                data = user.display_flight_id(flight_id)
                            except:
                                text = [
                                    "There was an issue with the Database.",
                                    "Please try again later",
                                ]
                            else:
                                if data != False:
                                    flight_columns2 = [a for a in flight_columns]
                                    flight_columns2.insert(0, "ID")

                                    table_printer(data, flight_columns2)
                                else:
                                    text = ["This Flight ID doesn't exist"]
                                    prompt(text)
                        else:
                            text = ["Please input an integer number!"]
                            prompt(text)
                    elif user_input == 2:
                        text = ["Please input the Flight Destination"]
                        prompt(text)
                        flight_destination = input("=> ")
                        try:
                            data = user.display_flight_destination(flight_destination)
                        except:
                            text = [
                                "There was an issue with the Database.",
                                "Please try again later",
                            ]
                            prompt(text)
                        else:
                            if data != False:
                                table_printer(data, flight_columns)
                            else:
                                text = ["This Flight Destination doesn't exist"]
                                prompt(text)

                    elif user_input == 3:
                        text = ["Please input the Flight Date. Format: YYYY MM DD"]
                        departure = input("=> ").split(" ")
                        if len(departure) == 3:
                            try:
                                departure = datetime.datetime(
                                    int(departure[0]),
                                    int(departure[1]),
                                    int(departure[2]),
                                )
                            except:
                                text = [
                                    "Thats not a correct date format!",
                                    "Please try again",
                                ]
                                prompt(text)
                            else:
                                try:
                                    data = user.display_flight_date(departure)
                                except:
                                    text = [
                                        "There was an issue with the Database.",
                                        "Please try again later",
                                    ]
                                    prompt(text)
                                else:
                                    if data != False:
                                        table_printer(data, flight_columns)
                                    else:
                                        text = ["This flight date doesn't exist"]
                                        prompt(text)
                        else:
                            text = ["Please use the correct format YYYY MM DD"]
                            prompt(text)
                    else:
                        text = ["That's not a valid option", "Please try again"]
                        prompt(text)
                else:
                    text = ["Please input an integer number!"]
                    prompt(text)
            elif choice == 4:
                text = ["Please input the Flight ID"]
                prompt(text)
                flight_id = input("=> ")
                if flight_id.isdigit():
                    flight_id = int(flight_id)
                    try:
                        data = user.display_flight_id(flight_id)
                    except:
                        text = [
                            "There was an issue with the Database.",
                            "Please try again later",
                        ]
                        prompt(text)
                    else:
                        if data != False:
                            text = [
                                f"There are {data[0][7]} available seats for Flight ID {flight_id}"
                            ]
                            prompt(text)
                        else:
                            text = ["This Flight ID doesn't exist"]
                            prompt(text)
                else:
                    text = ["Please input an integer number!"]
                    prompt(text)
            elif choice == 5:
                security_check(user)
            elif choice == 6:
                clear()
                break
            else:
                text = ["That's not a valid option", "Please try again"]
                prompt(text)

        else:
            text = ["Please input an integer number!"]
            prompt(text)


def user_management(user):
    clear()
    while True:
        text = [
            "-= User Management =-",
            "Select one of the options",
            "",
            "1. Add a new user",
            "2. Remove a user",
            "3. Edit user permissions",
            "4. View user information",
            "5. Go back",
        ]
        prompt(text)
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                text = ["Please provide a username and password for the new user."]
                prompt(text)
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
                    if data == False:
                        raise Exception()
                except:
                    print("Username not found.")
                else:
                    data = [a for a in data[0]]
                    final = []
                    for i in range(len(data)):
                        if i != 2:
                            final.append(str(data[i]))

                    user_columns = ["Index", "Username", "Staff ID", "Permissions"]
                    table_printer([final], user_columns)
            elif choice == 5:
                clear()
                break
            else:
                print("That's not a valid option\nPlease try again")
        else:
            print("Please input an integer number!")


def flight_management(user):
    clear()
    while True:
        text = [
            "-= Flight Management =-",
            "Select one of the options",
            "",
            "1. Add a new flight",
            "2. Remove a flight",
            "3. Edit a flight",
            "4. Go back",
        ]
        prompt(text)
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                text = ["Please input the following information:"]
                prompt(text)
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
                        if "time" in option:
                            text = ["Format: YYYY-MM-DD HH:MM"]
                            prompt(text)
                        user_input = input(
                            f"{str(display).replace('_', ' ').title()}: "
                        )
                        if user_input.isalpha() or "time" in option:
                            details[option] = user_input
                            break
                        elif user_input.isdigit():
                            details[option] = int(user_input)
                            break
                        else:
                            text = ["Not a valid input.", "Please try again"]
                            prompt(text)
                try:
                    user.add_flight(details, journey_columns)
                except:
                    text = [
                        "Failed to add the plane.",
                        "Check that your details are correct and try again.",
                    ]
                    prompt(text)
            elif choice == 2:
                text = ["Please input a flight ID number."]
                user_input = input("=> ")
                if user_input.isdigit():
                    try:
                        user.remove_flight(user_input)
                    except:
                        text = ["This flight doesn't exist."]
                        prompt(text)
                else:
                    text = ["Please input an integer number"]
                    prompt(text)
            elif choice == 3:
                text = ["Please input the information needed to perform an edit."]
                prompt(text)

                flight_ref = input("Flight ID: ")
                column = input("Column name: ")
                new_info = input("New information: ")

                if flight_ref.isdigit():
                    try:
                        user.edit_flight(flight_ref, column, new_info)
                    except:
                        text = ["This flight doesn't exist or wrong data was provided."]
                        prompt(text)
                else:
                    text = ["Please input an integer number for Flight ID"]
                    prompt(text)

            elif choice == 4:
                clear()
                break
            else:
                text = ["That's not a valid option", "Please try again"]
                prompt(text)

        else:
            text = ["Please input an integer number!"]
            prompt(text)


def plane_management(user):
    clear()
    while True:
        text = [
            "-= Plane Management =-",
            "Select one of the options",
            "",
            "1. Add a new plane",
            "2. Remove a plane",
            "3. Edit a plane",
            "4. Go back",
        ]
        prompt(text)
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                text = ["Please input the following information:"]
                prompt(text)
                details = {}
                plane_columns = [
                    "plane_type",
                    "plane_capacity",
                    "plane_size",
                    "fuel_capacity",
                    "speed",
                    "[weight]",
                    "seats_available",
                    "fuel_per_km",
                    "maintenance_date",
                ]
                for option in plane_columns:
                    display = option
                    while True:
                        if option == "maintenance_date":
                            text = ["Format: YYYY-MM-DD"]
                            prompt(text)

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
                            text = ["Not a valid input.", "Please try again"]
                            prompt(text)
                try:
                    user.add_plane(details, plane_columns)
                except:
                    text = [
                        "Failed to add the plane.",
                        "Check that your details are correct and try again.",
                    ]
                    prompt(text)

            elif choice == 2:
                text = ["Please input a plane ID number."]
                prompt(text)
                user_input = input("=> ")
                if user_input.isdigit():
                    try:
                        user.remove_plane(user_input)
                    except:
                        text = ["This plane doesn't exist."]
                        prompt(text)
                else:
                    text = ["Please input an integer number"]
                    prompt(text)
            elif choice == 3:
                text = ["Please input the information needed to perform an edit."]
                prompt(text)

                plane_ref = input("Plane ID: ")
                column = input("Column name: ")
                new_info = input("New information: ")

                if plane_ref.isdigit():
                    try:
                        user.edit_plane(plane_ref, column, new_info)
                    except:
                        text = ["This plane doesn't exist or wrong data was provided."]
                        prompt(text)
                else:
                    text = ["Please input an integer number for Plane ID"]
                    prompt(text)
            elif choice == 4:
                clear()
                break
            else:
                text = ["That's not a valid option", "Please try again"]
                prompt(text)

        else:
            text = ["Please input an integer number!"]
            prompt(text)


def admin_menu(user):
    clear()
    while True:
        text = [
            "-= Administrator Menu =-",
            "Select one of the options",
            "",
            "1. Staff Management",
            "2. Flight Management",
            "3. Plane Management",
            "4. Backup System",
            "5. Staff Actions",
            "6. Log out",
        ]
        prompt(text)
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
                text = [
                    "Please input the table you would like to back up and file name.",
                    "Acceptable format: '.json'",
                ]
                prompt(text)

                table_name = input("Table name: ")
                file_name = input("File name: ")

                if ".json" in file_name:
                    try:
                        user.backup_table(table_name, file_name)
                    except:
                        text = ["This table name doesn't exist."]
                        prompt(text)
                    else:
                        text = [f"{table_name} successfully backed up to {file_name}"]
                        prompt(text)
                else:
                    text = ["Unsuppored file format"]
                    prompt(text)

            elif choice == 5:
                staff_menu(user)
            elif choice == 6:
                clear()
                break
            else:
                text = ["That's not a valid option", "Please try again"]
                prompt(text)

        else:
            text = ["Please input an integer number!"]
            prompt(text)


def login_menu():
    clear()
    while True:
        text = ["-= Login =-", "Please input your login details"]
        prompt(text)
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        try:
            user = Staff(username, password)
            if user.permission_level == "admin":
                user = Admin(username, password)
        except:
            text = ["Login information incorrect!", "Please try again."]
            prompt(text)
            time.sleep(3)
        else:
            for i in range(3):
                clear()
                text = [f"Loading.{'.' * i}"]
                prompt(text)
                time.sleep(1)

            if user.permission_level == "user":
                staff_menu(user)
            elif user.permission_level == "admin":
                admin_menu(user)
            else:
                text = ["Permission Error.", "Please try again!"]
                prompt(text)
                time.sleep(3)
                break
            clear()
            break


def guest_menu():
    clear()
    user = Guest()
    flight_columns = [
        "Plane Type",
        "Departure Time",
        "Arrival Time",
        "Departing From",
        "Arriving To",
        "Capacity",
        "Seats Available",
        "Country",
        "Restrictions",
        "Visa",
    ]
    while True:
        text = [
            "-= Guest Menu =-",
            "See all the flights!",
            "",
            "1. View next 10 flights",
            "2. View flights to a specific destination",
            "3. View flights on a specific date",
            "4. Go Back",
        ]
        prompt(text)
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                data = user.all_flights()
                if data != False:
                    table_printer(data, flight_columns)
                else:
                    text = [
                        "We had an issue retriving flight data.",
                        "Please try again later.",
                    ]
                    prompt(text)

            elif choice == 2:
                text = [
                    "What destination are you interested in?",
                    "Please input a Country Code",
                ]
                prompt(text)
                destination = input("=> ")
                data = user.display_flight_destination(destination)
                if data != False:
                    table_printer(data, flight_columns)
                else:
                    text = ["That's not a valid destination.", "Please try again"]
                    prompt(text)

            elif choice == 3:
                text = ["What day would you like to fly?", "Format: YYYY MM DD"]
                prompt(text)
                departure = input("=> ").split(" ")
                if len(departure) == 3:
                    try:
                        departure = datetime.datetime(
                            int(departure[0]), int(departure[1]), int(departure[2])
                        )
                    except:
                        text = ["Thats not a correct date format!", "Please try again"]
                        prompt(text)
                    else:
                        data = user.display_flight_date(departure)
                        if data != False:
                            table_printer(data, flight_columns)
                        else:
                            text = ["That's not a valid date.", "Please try again"]
                            prompt(text)
                else:
                    text = ["Please use the correct format YYYY MM DD"]
                    prompt(text)

            elif choice == 4:
                user = None
                clear()
                break
            else:
                text = ["That's not a valid choice.", "Please try again"]
                prompt(text)
        else:
            text = ["Please input an integer number."]
            prompt(text)


def main():
    clear()
    while True:
        text = [
            "-= London Heathrow Airport =-",
            "Select one of the Options",
            "",
            "1. Guest Menu",
            "2. Login",
            "3. Exit",
        ]
        prompt(text)

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
                text = ["That's not a valid option", "Please try again"]
                prompt(text)

        else:
            text = ["Please input an integer number!"]
            prompt(text)


def prompt(text):
    top = "+" + "-" * 80 + "+"
    top_len = len(top)
    middle = math.floor((top_len - 1) / 2)

    print(top)
    for line in text:
        side = int(middle - (len(line) / 2))
        a = "|" + (" " * side) + line + (" " * side) + "|"
        if len(a) < 82:
            a = "|" + (" " * side) + line + (" " * (side + 1)) + "|"
        print(a)
    print(top)


def table_printer(data, columns):
    clear()
    table = PrettyTable()

    table.field_names = columns
    for row in data:
        table.add_row(row)
    print(table)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()