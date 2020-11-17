# Plane-Project

Parent Class

- Title
- First
- Last
- Address
- Date of birth

Child

- EXAMPLE
  - Passport
  - Visa
  - Ticket Number
  - etc

## Modules Breakdown

### Front Desk - Buy Tickets

#### Anonymous Querying

- Guest SQL Requests
- Select available flights
- Display available seats
- Pricings, Dates etc

#### Staff Querying

- Sell tickets
- Client data collection
- Automated system for checking if information is real
- Automated system for price altering for children / special cases

### Back end logic

- Admin Access
- Staff permission levels
- Ability to find client
- Alter client information
- Delete client information
- Remaining empty seats
- Login system (using SQL and Hashing)
- Local back up system into JSON

### Post Purchase / Entering airport or plane

- Check if ticket is valid
- Check if passport valid
- Check if visa needed
- Security Desk

## Naming conventions

- `main.py` = main front-end interface for user input
- `db_*.py` = backend class files containing database related - functionality
- `user_*.py` = Containers for each level of permissions and their actions
- `test_*.py` = test cases for the project
