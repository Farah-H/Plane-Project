USE plane_project;


CREATE TABLE countries (
    country_code VARCHAR(3) PRIMARY KEY,
    additional_restrictions VARCHAR(15),
    visa_restrictions VARCHAR(30),
);

CREATE TABLE passport_details (
    passport_id  VARCHAR(50) PRIMARY KEY,
    issue_date DATE NOT NULL,
    [expiry_date] DATE NOT NULL,
    expired BIT NOT NULL,
    country_code VARCHAR(3) REFERENCES countries(country_code),
    CONSTRAINT passport_details CHECK(
        [expiry_date] < GETDATE() OR expired = 1 
    )
);

CREATE TABLE passenger_details (
    passenger_id INT IDENTITY PRIMARY KEY,
    passport_id VARCHAR(30) NOT NULL REFERENCES passport_details(passport_id),
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    dob DATE NOT NULL,
    dependent_on VARCHAR(15) REFERENCES passenger_details(passenger_id),
    CONSTRAINT passenger_details CHECK
    (DATEDIFF(year, GETDATE(), dob) <= 12 OR dependent_on IS NOT NULL)
);


CREATE TABLE airports(
    airport_code VARCHAR(4) PRIMARY KEY,
    country_code VARCHAR(3) NOT NULL REFERENCES countries(country_code),
    longitude DECIMAL(9,6) NOT NULL,
    latitude DECIMAL(8,6) NOT NULL, 
    

);