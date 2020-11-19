import os
import getpass
import time
from user_guest import Guest
from user_staff import Staff
from user_admin import Admin


def booking(user):
    pass


def staff_menu(user):
    clear()
    while True:
        print(
            """
-= Staff Menu =-
Select one of the options

1. Book a flight
2. Change passenger information
3. Display passenger information
4. Display flight information
5. Check available seats
6. Security Check
7. Log out
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
                break
            else:
                print("That's not a valid option\nPlease try again")

        else:
            print("Please input a integer number!")


def admin_menu(user):
    clear()
    while True:
        print(
            """
-= Administrator Menu =-
Select one of the options

1. Add staff member
2. Remove staff member
3. Change user's permissions
4. View user informations
5. Add flight
6. Remove flight
7. Edit flight information
8. Backup a database table to a file
9. Log out
        """
        )
        choice = input("=> ")
        if choice.isdigit():
            choice = int(choice)

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
                pass
            elif choice == 6:
                pass
            elif choice == 7:
                pass
            elif choice == 8:
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

            elif choice == 9:
                break
            else:
                print("That's not a valid option\nPlease try again")

        else:
            print("Please input a integer number!")


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
                break
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
                time.sleep(5)

            elif choice == 2:
                print("What destination are you interested in?")
                destination = input("=> ")
                data = user.display_flight("journey_details.arriving_to", destination)
                if data != False:
                    ## FORMATTING NEEDED
                    print(data)
                else:
                    print("That's not a valid destination.\nPlease try again")
                time.sleep(5)

            elif choice == 3:
                print("What day would you like to fly?\nFormat: YYYY MM DD")
                departure = input("=> ").split(" ")
                if len(departure) == 3:
                    data = user.display_flight(
                        "journey_details.departure_time", departure
                    )
                    if data != False:
                        ## FORMATTING NEEDED
                        print(data)
                    else:
                        print("That's not a valid date.\nPlease try again")
                else:
                    print("Please use the correct format YYYY MM DD")
                time.sleep(5)

            elif choice == 4:
                user = None
                break
            else:
                print("That's not a valid choice.\nPlease try again")
        else:
            print("Please input an integer number.")


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
                break
            else:
                print("That's not a valid option\nPlease try again")

        else:
            print("Please input a integer number!")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()