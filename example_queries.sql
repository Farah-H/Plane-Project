USE plane_project;


-- ADD A NEW FLIGHT JOURNEY

INSERT INTO journey_details (
    plane_id,
    departure_time,
    arrival_time,
    departing_from,
    arriving_to
)

VALUES (
    6,
    '2020-06-15 00:00',
    '2020-06-15 00:00',
    'LHR',
    'SCH'
);

-- ADD A NEW PLANE
INSERT INTO planes (
    plane_type,
    plane_capacity,
    plane_size,
    fuel_capacity,
    speed,
    [weight], -- what units...? 
    seats_available,
    fuel_per_km,
    maintenance_date
)

VALUES (
    'plane',
    350,
    'M',
    30,
    700,
    16000,
    300,
    1,
    '2020-12-31'
);

-- ADD A BOOKING
-- you gotta do a bunch of checks to make sure u dont end up with errors

-- 1. check if passport  is already in DB
-- this will return 0 if the passport is not in the DB, so u can just do if False in python, or 1 if it is, for True
SELECT COUNT(*) FROM passport_details WHERE passport_id = '234whatever';

-- 2. check if passport is expired: This returns 1 if the passport is valid for travel
SELECT COUNT(*) FROM passport_details WHERE passport_id = 'EG248966' and expired = 1;

-- 3. If passport is expired / doesn't exist, create a new passport 
INSERT INTO passport_details (
    passport_id,
    issue_date,
    [expiry_date],
    expired,
    country_code
)

VALUES (
    '89374fasdsk',
    '2017-03-02',
    '2020-09-01',
    1,
    'BE'
);

-- 4. add passenger details
INSERT INTO passenger_details (
    passport_id,
    first_name,
    last_name,
    dob 
)

VALUES (
    '89374fasdsk',
    'Hisham',
    'Malek',
    '1997-04-05' 
);

-- 5. create a booking

INSERT INTO booking_details (
    booking_date,
    staff_id,
    airline,
    total
)

VALUES (
    '2020-08-11 15:23:44',
    2,
    'British Airways',
    67.98
);

-- 6. create ticket details, 

INSERT INTO ticket_details(
    journey_id,
    seat_number,
    terminal_id,
    passenger_id,
    booking_id
)

VALUES (
    3,
    'A231',
    NULL,
    1,
    1
);

SELECT * FROM credentials;


-- query that displays all the information about specific flight (with journey_id)
SELECT journey_details.journey_id,
    journey_details.departing_from,
    journey_details.departure_time,
    journey_details.arriving_to,
    journey_details.arrival_time,
    planes.seats_available
FROM journey_details
INNER JOIN planes on journey_details.plane_id = planes.plane_id;

-- view passenger information
SELECT passenger_details.first_name,
    passenger_details.last_name,
    passenger_details.dob,
    passenger_details.passport_id
FROM passenger_details
INNER JOIN ticket_details on ticket_details.passenger_id = passenger_details.passenger_id
WHERE ticket_details.journey_id = '2';