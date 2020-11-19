import os
import getpass
import time
import datetime
from user_guest import Guest
from user_staff import Staff
from user_admin import Admin


def booking(user):
    clear()
    while True:
        print(
            """

            """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            pass


def staff_menu(user):
    clear()
    while True:
        print(
            f"""
-= Staff Menu =-
Select one of the options

1. Book a flight
2. Change passenger information
3. Display passenger information
4. Display flight information
5. Check available seats
6. Security Check
7. {"Log out" if user.permission_level == "user" else "Go Back"}
        """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                booking(user)
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                pass
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
            if choice == 1:
                print("Please provide a username and password for the new user.")
                username = input("Username: ")
                password = input("Password: ")

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
                    "maintenance_data",
                ]
                for option in plane_columns:
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
                        departure = datetime.datetime(
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
3. Exit"""
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


def clear():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()