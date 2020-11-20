-- Adding some sample data to test the DB, starting with one line for now
-- Once everything is working, will use data generator to put in more rows 


-- -- hashed passwords to test security system
-- INSERT INTO credentials (username, [password], [permissions] )
-- VALUES ('dev','bbde1660026930e8bfb5c4570cc703d6e4b83614d8a3f33483e5207915c21615f9f66fac152e3dde6fc39ac83243249cfa137f813f50be9b77fa445533efcdc318257bb351a7677bb002a5f1833b97e12972c02c6df6ca33ed062ae2e43df44c', 'admin');

-- INSERT INTO credentials (username, [password], [permissions] )
-- VALUES ('farah','086f6d907660708974d73b17e0eb022e33e13a49947030228cc84ed876c223ced45bb299e81fd37f2edcd08b972308f267c117ef3d074f85f336d6944e69be4290001858b37cd75e02473c8efdaf35651d18fd5cb97e3e69ce0ac65fbb9fc4f8', 'admin');

-- INSERT INTO credentials (username, [password], [permissions] )
-- VALUES ('jamie','a939db16d5f9856043c35bcb3253bb4e56733a4478719cc078f395dc75381d7f0abe02a6a4d3ffa9952a50b3aca9d50c39268fd562fb61b2734cc10101f3f8f5d60748fc40932c60f01469f8c8026b74ef59f2e7bf4d0fb1423c12bda2302851', 'user');

-- INSERT INTO credentials (username, [password], [permissions] )
-- VALUES ('jake','a9e43cd6c8569a77b4558f3b9f115504cb4b44e41d0557dcf7e91c9ede7932b2f85fb551a9fccbced944e1286e5b9430f5f7ba8c01e063e520f7f2225a3eef6a5dfd1d4d7dd236ed7b8b39306cdf4a70c9392ab477cb5954e7eff06d30abd502', 'user');

-- INSERT INTO credentials (username, [password], [permissions] )
-- VALUES ('guest','3444b66b8aa5660d69d0e2e54a519e36ace4fa7a6a2845f817ab930de92a58604ddab17cfb3eaf6610226a166466bdc637bab11464325e129cca47362afd39c5c47e685274f348f726495c532abd2a1d7dac33e99a41348b894ba3024ff22044', 'guest');



-- adding things in the order country, passportdetails,passenger_details, airports, staff, creds, terminals, planes, journeydetails, bookingsdetails, ticket details
USE plane_project;
-- country
INSERT INTO country (
    country_code,
    country_name,
    additional_restrictions,
    visa_restrictions
)

VALUES (
    'CN',
    'China',
    NULL, -- essential travel only, might make a table for restrictions but not necessary atm
    'All' -- again, i could probably make a table for levels of visa restrictions etc. and idetify using a code
);

SELECT * FROM country;
-- passport details, add another one later which is expired for tests
INSERT INTO passport_details (
    passport_id,
    issue_date,
    [expiry_date],
    expired,
    country_code
)

VALUES (
    '89374fasdsk',
    '2017-03-2',
    '2020-09-01',
    1,
    'BE'
);


-- passenger details 
INSERT INTO passenger_details (
    passport_id,
    first_name,
    last_name,
    dob -- add dependent on constraint for age =< 12 later
)

VALUES (
    'EG248966',
    'Hisham',
    'Malek',
    '1997-04-05' -- date input must be taken as 'YYYY-MM-DD'
);

-- airports
INSERT INTO airports (
    airport_code,
    country_code,
    latitude,
    longitude
)

VALUES (
    'SCH',
    'NL',
    51.670020,
    -0.434295
);

SELECT * FROM airports;
-- staff
INSERT INTO staff (
    first_name,
    last_name,
    dob,
    [role]
)

VALUES (
    'Hubert',
    'Swic',
    '1998-03-17',
    'Airport Assistant'
);

SELECT * FROM staff;
SELECT * FROM credentials;
UPDATE credentials SET staff_id = 4 where username = 'dev';

-- -- creds

-- INSERT INTO credentials (
--     username, 
--     [password],
--     staff_id,
--     [permissions]
-- )

-- VALUES (
--     'staff me',
--     'abcd',
--     2,
--     'user'
-- );



-- terminals
INSERT INTO terminals (
    airport_code,
    terminal_capacity,
    runway_size
)

VALUES (
    'LH',
    500,
    'L' -- this doesn't make sense, maybe change later to smt more descriptive / more easily compared with plane size
);

UPDATE terminals SET runway_size = 'M' where terminal_id = 1
SELECT * FROM terminals;
-- planes
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
    8,
    '2020-12-31'
);

SELECT * FROM planes;
--journeydetails
INSERT INTO journey_details(
    plane_id,
    departure_time,
    arrival_time,
    departing_from,
    arriving_to
)

VALUES (
    8,
    '2020-11-19 09:00',
    '2020-11-19 10:00',
    'LHR',
    'GAT'
);

SELECT * FROM terminals;

SELECT * FROM planes;
--bookingdetails

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

UPDATE planes SET seats_available = 7 where plane_type = 'helicopter';
--ticketdetails
INSERT INTO ticket_details(
    journey_id,
    seat_number,
    terminal_id,
    passenger_id,
    booking_id
)

VALUES (
    3,
    'F231',
    1,
    1,
    1
);
USE plane_project;
SELECT * FROM journey_details;



SELECT TABLE_NAME, FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE';


SELECT * FROM INFORMATION_SCHEMA.COLUMNS;



USE plane_project;
ALTER TABLE ticket_details
ALTER COLUMN booking_id INT NOT NULL;

SELECT * FROM booking_details;