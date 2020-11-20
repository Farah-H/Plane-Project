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
