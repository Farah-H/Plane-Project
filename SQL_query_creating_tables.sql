USE plane_project;


CREATE TABLE country_details (
    country_code VARCHAR(3) PRIMARY KEY,
    country_name VARCHAR(100) UNIQUE,
    additional_restrictions VARCHAR(15),
    visa_restrictions VARCHAR(30),
);

CREATE TABLE passport_details (
    passport_id  VARCHAR(50) PRIMARY KEY,
    issue_date DATE NOT NULL,
    [expiry_date] DATE NOT NULL,
    expired BIT NOT NULL,
    country_code VARCHAR(3) REFERENCES countries(country_code),
    -- CONSTRAINT passport_details CHECK(
    --     [expiry_date] < GETDATE() OR expired = 1 
    -- )
);

USE plane_project;

CREATE TABLE passenger_details (
    passenger_id INT IDENTITY PRIMARY KEY,
    passport_id VARCHAR(50) NOT NULL REFERENCES passport_details(passport_id),
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    dob DATE NOT NULL,
    dependent_on INT REFERENCES passenger_details(passenger_id),
    CONSTRAINT passenger_details CHECK
    (DATEDIFF(year, GETDATE(), dob) <= 12 OR dependent_on IS NOT NULL)
);


CREATE TABLE airports(
    airport_code VARCHAR(4) PRIMARY KEY,
    country_code VARCHAR(3) NOT NULL REFERENCES country_details(country_code),
    longitude DECIMAL(9,6) NOT NULL,
    latitude DECIMAL(8,6) NOT NULL, 

);

CREATE TABLE staff (
    staff_id INT IDENTITY PRIMARY KEY,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    dob DATE NOT NULL,
    [role] VARCHAR(30)
);

CREATE TABLE credentials (
    [user_id] INT IDENTITY PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    [password] VARCHAR(255) NOT NULL,
    staff_id INT NOT NULL REFERENCES staff(staff_id),
    [permissions] VARCHAR(5) NOT NULL
);

CREATE TABLE terminals (
    terminal_id INT IDENTITY PRIMARY KEY,
    airport_code VARCHAR(4) NOT NULL REFERENCES airports(airport_code),
    terminal_capacity INT NOT NULL,
    runway_size VARCHAR(10) NOT NULL
);

CREATE TABLE planes (
    plane_id INT IDENTITY PRIMARY KEY,
    plane_type VARCHAR(10),
    plane_capacity INT NOT NULL,
    plane_size VARCHAR(4) NOT NULL,
    fuel_capacity INT NOT NULL,
    speed INT NOT NULL,
    [weight] INT NOT NULL,
    seats_available BIT NOT NULL,
    fuel_per_km INT NOT NULL,
    maintenance_date DATE
);

CREATE TABLE journey_details (
    journey_id INT IDENTITY PRIMARY KEY,
    plane_id INT REFERENCES planes(plane_id),
    departure_time DATETIME,
    arrival_time DATETIME,
    departing_from VARCHAR(4) REFERENCES airports(airport_code),
    arriving_to VARCHAR(4) REFERENCES airports(airport_code),

);

CREATE TABLE booking_details (
    booking_id INT IDENTITY PRIMARY KEY,
    booking_date DATETIME NOT NULL,
    staff_id INT NOT NULL REFERENCES staff(staff_id),
    airline VARCHAR(25) NOT NULL,
    total MONEY NOT NULL

);

CREATE TABLE ticket_details (
    ticket_id INT IDENTITY PRIMARY KEY,
    journey_id INT REFERENCES journey_details(journey_id),
    seat_number VARCHAR(4),
    terminal_id INT REFERENCES terminals(terminal_id),
    passenger_id INT REFERENCES passenger_details(passenger_id),
    booking_id INT REFERENCES booking_details(booking_id)
)