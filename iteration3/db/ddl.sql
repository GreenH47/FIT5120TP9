CREATE TABLE council.Postcode (
  locality_name VARCHAR(255) NOT NULL,
  postcode INT NOT NULL,
  council_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (postcode)
);

CREATE TABLE council.Bin (
  council_name VARCHAR(500) NOT NULL,
  landfill_yes VARCHAR(500) NOT NULL,
  landfill_no VARCHAR(500) NOT NULL,
  recycle_yes VARCHAR(500) NOT NULL,
  recycle_no VARCHAR(500) NOT NULL,
  green_yes VARCHAR(500) NOT NULL,
  green_no VARCHAR(500) NOT NULL,
  council_name_fk VARCHAR(255) NOT NULL,
  FOREIGN KEY (council_name_fk) REFERENCES council.Postcode (council_name)
);

CREATE TABLE council.Waste (
  year INT NOT NULL,
  council_name VARCHAR(255) NOT NULL,
  waste_pp FLOAT NOT NULL,
  garbage_pp FLOAT NOT NULL,
  recycle_pp FLOAT NOT NULL,
  organic_pp FLOAT NOT NULL,
  collect_type VARCHAR(255) NOT NULL,
  amount INT NOT NULL,
  diversion_rate FLOAT NOT NULL,
  council_name_fk VARCHAR(255) NOT NULL,
  FOREIGN KEY (council_name_fk) REFERENCES council.Postcode (council_name)
);

CREATE TABLE council.calendar (
  street_name VARCHAR(255) NOT NULL,
  council_name VARCHAR(255) NOT NULL,
  landfill_frequency VARCHAR(255) NOT NULL,
  landfill_next DATE NOT NULL,
  recycle_frequency VARCHAR(255) NOT NULL,
  recycle_next DATE NOT NULL,
  green_frequency VARCHAR(255) NOT NULL,
  green_next DATE NOT NULL,
  council_name_fk VARCHAR(255) NOT NULL,
  FOREIGN KEY (council_name_fk) REFERENCES council.Postcode (council_name)
);

create table council.Policy
(
    waste_type   varchar(255) null,
    council_name varchar(255) null,
    waste_policy varchar(255) null,
    council_name_fk VARCHAR(255) NOT NULL,
    FOREIGN KEY (council_name_fk) REFERENCES council.Postcode (council_name)
);
