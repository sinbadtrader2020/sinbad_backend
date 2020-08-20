-----------------------------
----------- TYPE  -----------
-----------------------------

CREATE TYPE SF_LANGUAGE AS ENUM (
    'ENGLISH',
    'BANGLA',
    'ARABIC',
    'CHINESE'
);

CREATE TYPE SF_STATUS AS ENUM (
    'ACTIVE',
    'INACTIVE'
);

-----------------------------
----------- TABLE -----------
-----------------------------

CREATE TABLE sf_user (
  id                        SERIAL PRIMARY KEY,
  first_name                TEXT NOT NULL,
  last_name                 TEXT NOT NULL,
  email                     TEXT NOT NULL UNIQUE,
  mobile_number             TEXT NOT NULL,
  password                  TEXT NOT NULL,
  street_address            TEXT,
  city                      TEXT,
  country                   TEXT,
  zip_code                  TEXT,
  language                  SF_LANGUAGE DEFAULT 'ENGLISH',
  user_create               DATE,
  status                    SF_STATUS DEFAULT 'ACTIVE'
);

-----------------------------
----------- VIEW  -----------
-----------------------------

CREATE OR REPLACE VIEW sf_user_view AS
select id, first_name, last_name, email, street_address, city, mobile_number, language, user_create, zip_code, status from sf_user;