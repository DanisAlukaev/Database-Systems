CREATE TABLE IF NOT EXISTS customer1
(
    id      SERIAL PRIMARY KEY NOT NULL,
    name    TEXT               NOT NULL,
    address TEXT               NOT NULL,
    age     INT                NOT NULL,
    review  TEXT
);

CREATE TABLE IF NOT EXISTS customer2
(
    id      SERIAL PRIMARY KEY NOT NULL,
    name    TEXT               NOT NULL,
    address TEXT               NOT NULL,
    age     INT                NOT NULL,
    review  TEXT
);
