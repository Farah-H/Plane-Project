# Plane-Project Test
Each heading will have a list of tests that need to be created to check the functionality behind our project works as
 intended. Each bullet point is a new test, bullet points with question marks at the start are speculative and need
  to be clarified with the teammate creating that class. Questions with an exclamation mark in front of them are not
   tests that can be written in python, they are focused on the user experience and whether the system is easy to
    understand and use.
## ClientInformation class tests
- If we use a getter for any of the class attributes, it should return the attribute for that instance
- Should be a fullname() method that returns the users full name including their title to easily output this to the user
## Connection class tests
- If we instantiate the class does it successfully create a connection with the database
## Authentication class tests
- If we call the credential_manager() method with a username we should be able to get data for that user, and if the
 user is not found we should return False
- If we call the check_login() method we should return the permissions associated with that user if the user
 can log in (i.e. they have supplied the correct username and password), and if not we should get a False value returned
- If we call the db_credentials() method we should check if the correct values (the users username, and their
 permissions level) when called, assuming that the users details can be found, if not an exception should be raised
 - If we pass a username and a new password for that username it should return True if the username is found in the
  database and we should be able to check that the password has been changed. If the username cannot be found then we
   should return False
## BackupData class (Still not complete)
- When the backup_handler() class is called can you successfully retrieve the data stored in the database
    - If not, does the method handle this gracefully (i.e. no errors)
    - If something happens to the database can we recreate the data with a constructor() method?
## Admin class
- When calling the add_staff() method we should be able to add a new staff member and get True returned from the
 method if this is successful, and False if this was unsuccessful (e.g. if the staff member already exists)
- When calling the remove_staff() method we should be able to get a returned value of True if the staff member was
 successfully removed, and False if there was an issue (e.g. removing a staff member that does not exist)
- When calling the change_permissions() method we should get a returned value of True when trying to change an
 existing staff member from user to an admin or vice versa. We should get a returned value of False when trying to
  change a non existent user's permissions, or when trying to change a user's permissions to user or an admin's
   permissions to admin
- When trying to view a user's records in the view_user() method, the returned list should match that user's data from
 database. If the user's data cannot be found we should return False.
- When calling the edit_flight() method we should get a returned value of True if the passed data is correct and was
 successfully input into the database. When attempting to edit a flight that doesn't exist we should return False. We
  should also return False when a data type other than a dictionary is passed to the function or if the dictionary's
   key names do not match those expected
- When trying to add a flight with the add_flight() method, we should return True if the data is all correct, and
 False if there are issues with the data (e.g. destinations and departure locations that aren't in the database
 , references to flights that don't exist, etc.)
## Guests class
- 
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

## Front end UI tests
- Are the attributes in the ```__init__``` method validated e.g. a negative flight duration or an arrival time before
 the departure time
- Are the departure and arrival times going to be strings or datetime objects?
- Is the body method meant to be inside the Flight class?
- Good handling of invalid options with except: continue block
- Are the ifs and elifs in the loops?
- Infinite loop when making choices?
    - Except statement only runs when a user inputs a non numeric, doesn't cover if the user inputs numbers that aren't 
      1, 2, or 3
- Check email address for the inclusion of the '@' character to validate it
- Check for non yes or no responses to the minor question
- When receiving the minor's date of birth we should check to see if they're young enough to be considered a minor
, otherwise we could lose money (we should also specify the cutoff age before asking if they are travelling with any
 minors)
- No message on what the user should input for ```departure_date```
- Good check on the validity of the departure and landing destinations
## 
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
## ?Security tests
- Does the check_passport() function correctly identify valid and non valid passports i.e. checking the expiration
 date, or observations state they can't travel to certain countries, or their name/other personal details do not
  match the ones given at the airport
- Can the check_visa() function correctly query the database to see if the destination country requires a visa?
    - Can the function then validate the user's visa