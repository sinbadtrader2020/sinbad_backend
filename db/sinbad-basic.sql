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
  city                      TEXT,
  country                   TEXT,
  mobile_number             TEXT,
  language                  SF_LANGUAGE DEFAULT 'ENGLISH',
  password                  TEXT,
  user_create               DATE,
  status                    SF_STATUS DEFAULT 'ACTIVE'
);

-----------------------------
----------- VIEW  -----------
-----------------------------

CREATE OR REPLACE VIEW sf_user_view AS
select id, first_name, last_name, email, city, mobile_number, language, user_create, status from sf_user;