# Plane Project Database (DB) Guide

__The purpose of this document is to explain the order in which to carry out SQL queries when fulfilling the user stories.__ You can take the inputs from the user / assistant in any order you want, but you must query in this order, otherwise the DB will return errors due to foreign key and NOT NULL constraints. 

## DB Structure
![](DB_design.png)

To abstract querying this DB in python, please refer to the `DB_struture_plan.xlsx` file, which explicitly states the type inputs required in python, e.g `airport_code : STRING max, length = 4, upper,alpha`

## User Stories
### 1. As an airport assistance I want to be able to create a passenger with a name and Passport number so that I can add them to the flight. 

__you must insert passport details before personal info like age / name etc.__ Also passport number = passport_id because by definition passport numbers are unique. 


- take user's passport number / `passport_id`
- check whether it exists in in `passport_details` table
    - if it exists but `expired == True`, skip personal details info, but get new passport details from them. (see below)
    - if it exists and `expired == False` do nothing, they are already in the DB and their passport is valid for travel. 
    - if it doesn't exist:
        - create new passport record using their `passport_id`, `issue_date`, `expiry_date`, False, `country_code` for issuing country. 
        - take their personal details, and create a record in the `passenger_details` table, you need their `passport_id`, 