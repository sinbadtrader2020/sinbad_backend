-----------------------------
----------- TYPE  -----------
-----------------------------

CREATE TYPE HT_LANGUAGE AS ENUM (
    'ENGLISH',
    'BANGLA',
    'ARABIC',
    'CHINESE'
);

CREATE TYPE HT_STATUS AS ENUM (
    'ACTIVE',
    'INACTIVE'
);

-----------------------------
----------- TABLE -----------
-----------------------------

CREATE TABLE ht_user (
  id                        SERIAL PRIMARY KEY,
  first_name                TEXT NOT NULL,
  last_name                 TEXT NOT NULL,
  email                     TEXT NOT NULL UNIQUE,
  city                      TEXT,
  country                   TEXT,
  mobile_number             TEXT,
  language                  HT_LANGUAGE DEFAULT 'ENGLISH',
  password                  TEXT,
  user_create               DATE,
  status                    HT_STATUS DEFAULT 'ACTIVE'
);

-----------------------------
----------- VIEW  -----------
-----------------------------