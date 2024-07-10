-- create the database to use
CREATE DATABASE water_quality_db;

-- Create the WaterQuality table
CREATE TABLE WaterQuality (
    id SERIAL PRIMARY KEY,
    ph FLOAT NOT NULL DEFAULT 0,
    Hardness FLOAT NOT NULL DEFAULT 0,
    Solids FLOAT NOT NULL DEFAULT 0,
    Chloramines FLOAT NOT NULL DEFAULT 0,
    Sulfate FLOAT NOT NULL DEFAULT 0,
    Conductivity FLOAT NOT NULL DEFAULT 0,
    Organic_carbon FLOAT NOT NULL DEFAULT 0,
    Trihalomethanes FLOAT NOT NULL DEFAULT 0,
    Turbidity FLOAT NOT NULL DEFAULT 0
);


-- Create the WaterPotability table
CREATE TABLE WaterPotability (
    id SERIAL PRIMARY KEY,
    water_quality_id INT REFERENCES WaterQuality(id),
    Potability INT
);

