CREATE TABLE IF NOT EXISTS customer_btree
(
    ID      SERIAL PRIMARY KEY NOT NULL,
    Name    TEXT               NOT NULL,
    Address TEXT               NOT NULL,
    Review  TEXT
);

CREATE TABLE IF NOT EXISTS customer_hash
(
    ID      SERIAL PRIMARY KEY NOT NULL,
    Name    TEXT               NOT NULL,
    Address TEXT               NOT NULL,
    Review  TEXT
);
