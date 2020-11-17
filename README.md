# Plane-Project Test
Each heading will have a list of tests that need to be created to check the functionality behind our project works as
 intended. Each bullet point is a new test, bullet points with question marks at the start are speculative and need
  to be clarified with the teammate creating that class. Questions with an exclamation mark in front of them are not
   tests that can be written in python, they are focused on the user experience and whether the system is easy to
    understand and use.
## ClientInformation class tests
- If we use a getter for any of the class attributes, it should return the attribute for that instance
- ?If we use a setter for any of the class attributes, it should change that attribute for that instance
- Should be a fullname() method that returns the users full name including their title
## Authentication class tests
- If we instantiate the class does it successfully create a connection with the database
## BackupData class
- When the backup_handler() class is called can you successfully retrieve the data stored in the database
    - If not, does the method handle this gracefully (i.e. no errors)
    - If something happens to the database can we recreate the data with a constructor() method?
## Passenger class tests
- When initialised, are the passengers information for their Passport, Visa, and Ticket Number assigned correctly?
- If we call the ```set_personal_info()``` method, are the attributes set accordingly
    - Does this method handle invalid inputs e.g. having a date of birth in the future
    - Can it cope with inputting information in different formats i.e. having dob be 01/01/1956 but also 01-01-1956
    , and if not is it specified to the user which format is desired?
    - Because this is a system to be used by people from all over the world, does it account for different dob orders
     i.e. "DD/MM/YYYY" vs "MM/DD/YYYY" in different countries, and if not does it make it clear which order the user
      should use when inputting this?
- !Is it clear what the user is inputting for each attribute and what form it should take?
## StaffMember class
- Can the StaffMember log in to be able to perform tasks that only Staff can perform?
- Can a StaffMember change their details e.g. regularly changing their passwords to ensure the system is secure?
    - If a StaffMember tries to change their password and inputs their existing password they should be told that
     their new password must be different from their last password
## AirportAssistant class
- Can the create_passenger() function retrieve and use a Passenger's name and Passport details
    - Can they then add that Passenger to a Flight?
- Can the flight_trip() function create a trip with a plane, departure location, destination, and date?
    - Does it allow an AirportAssistant to create a trip that overlaps with another trip by the same plane e.g
    . setting a flight trip from France to Germany on the 5th of December when that same plane is already making a
     trip from Senegal to Brazil from the 4th to the 6th?
- Can they UPDATE the flight_trip information using the inherited ClientInformation connection method?
- If a StaffMember or a Passenger without the right permissions attempts to execute any of the above functionality
, does this work?

## Flight class tests

## Seat class tests
- Does the ```__init__``` method correctly assign the passed arguments to the instance?
    - ?If the seat number already exists, is there a check here for that or is that handled elsewhere?
        - ?If this is handled here, does the initialiser handle this gracefully?
- If the ```__str__``` method is called does it return the correct values?

## ?Security tests
- Does the check_passport() function correctly identify valid and non valid passports i.e. checking the expiration
 date, or observations state they can't travel to certain countries, or their name/other personal details do not
  match the ones given at the airport
- Can the check_visa() function correctly query the database to see if the destination country requires a visa?
    - Can the function then validate the user's visa