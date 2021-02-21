CREATE TABLE IF NOT EXISTS customer_btree
(
    id      SERIAL PRIMARY KEY NOT NULL,
    name    TEXT               NOT NULL,
    address TEXT               NOT NULL,
    age     INT                NOT NULL,
    review  TEXT
);

CREATE TABLE IF NOT EXISTS customer_hash
(
    id      SERIAL PRIMARY KEY NOT NULL,
    name    TEXT               NOT NULL,
    address TEXT               NOT NULL,
    age     INT                NOT NULL,
    review  TEXT
);
