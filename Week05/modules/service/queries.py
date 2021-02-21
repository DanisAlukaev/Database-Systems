import os


class Queries:
    SELECT_ALL_BTREE = "SELECT * FROM customer_btree;"
    SELECT_ALL_HASH = "SELECT * FROM customer_hash;"
    ADD_CUSTOMER_BTREE = "INSERT INTO customer_btree(name, address, age, review) VALUES (%s, %s, %s, %s);"
    ADD_CUSTOMER_HASH = "INSERT INTO customer_hash(name, address, age, review) VALUES (%s, %s, %s, %s);"
    INDEX_BTREE_AGE = "CREATE INDEX ON customer_btree USING BTREE (age);"
    INDEX_HASH_AGE = "CREATE INDEX ON customer_hash USING HASH (age);"
    INDEX_BTREE_NAME = "CREATE INDEX ON customer_btree USING BTREE (name);"
    INDEX_HASH_NAME = "CREATE INDEX ON customer_hash USING HASH (name);"
    ANALYZE_BTREE_AGE = "EXPLAIN ANALYZE SELECT * FROM customer_btree WHERE age >= 18 and age <= 30;"
    ANALYZE_HASH_AGE = "EXPLAIN ANALYZE SELECT * FROM customer_hash WHERE age >= 18 and age <= 30;"
    ANALYZE_BTREE_NAME = "EXPLAIN ANALYZE SELECT * FROM customer_btree WHERE name ~ 'A.+';"
    ANALYZE_HASH_NAME = "EXPLAIN ANALYZE SELECT * FROM customer_hash WHERE name ~ 'A.+';"

    def __init__(self, connection_db):
        self.connection_db = connection_db

    def create_tables(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                create_query = open("./modules/service/database.sql", "r").read()
                cursor.execute(create_query)

    def select_all_btree(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.SELECT_ALL_BTREE
                cursor.execute(command)

    def select_all_hash(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.SELECT_ALL_HASH
                cursor.execute(command)

    def add_customer_btree(self, name, address, age, review):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ADD_CUSTOMER_BTREE
                args = name, address, age, review
                cursor.execute(command, args)

    def add_customer_hash(self, name, address, age, review):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ADD_CUSTOMER_HASH
                args = name, address, age, review
                cursor.execute(command, args)

    def index_btree_age(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.INDEX_BTREE_AGE
                cursor.execute(command)

    def index_hash_age(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.INDEX_HASH_AGE
                cursor.execute(command)

    def index_btree_name(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.INDEX_BTREE_NAME
                cursor.execute(command)

    def index_hash_name(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.INDEX_HASH_NAME
                cursor.execute(command)

    def analyze_btree_age(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ANALYZE_BTREE_AGE
                cursor.execute(command)
                print('B-tree: ', cursor.fetchall()[0][0])

    def analyze_hash_age(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ANALYZE_HASH_AGE
                cursor.execute(command)
                print('Hash:  ', cursor.fetchall()[0][0])

    def analyze_btree_name(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ANALYZE_BTREE_NAME
                cursor.execute(command)
                print('B-tree: ', cursor.fetchall()[0][0])

    def analyze_hash_name(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ANALYZE_HASH_NAME
                cursor.execute(command)
                print('Hash:  ', cursor.fetchall()[0][0])
