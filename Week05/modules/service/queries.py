import os


class Queries:
    SELECT_ALL_BTREE = "SELECT * FROM customer_btree"
    SELECT_ALL_HASH = "SELECT * FROM customer_hash"
    ADD_CUSTOMER_BTREE = "INSERT INTO customer_btree(Name, Address, Age, Review) VALUES (%s, %s, %s, %s);"
    ADD_CUSTOMER_HASH = "INSERT INTO customer_hash(Name, Address, Age, Review) VALUES (%s, %s, %s, %s);"
    SELECT_ADULTS_BTREE = "SELECT * FROM customer_btree WHERE Age >= 18"
    SELECT_ADULTS_HASH = "SELECT * FROM customer_hash WHERE Age >= 18"
    CREATE_INDEX_BTREE = "CREATE INDEX ON customer_btree (Age)"
    CREATE_INDEX_HASH = "CREATE INDEX ON customer_hash (Age)"
    ANALYZE_BTREE = "EXPLAIN ANALYZE SELECT * FROM customer_btree WHERE Age >= 18 and Age <= 30"
    ANALYZE_HASH = "EXPLAIN ANALYZE SELECT * FROM customer_hash WHERE Age >= 18 and Age <= 30"

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

    def select_adults_btree(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.SELECT_ADULTS_BTREE
                cursor.execute(command)

    def select_adults_hash(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.SELECT_ADULTS_HASH
                cursor.execute(command)

    def performance_select_adults_btree(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ANALYZE_BTREE
                cursor.execute(command)
                print('B-tree: ', cursor.fetchall()[0][0])

    def performance_select_adults_hash(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ANALYZE_HASH
                cursor.execute(command)
                print('Hash:  ', cursor.fetchall()[0][0])

    def create_index_age_btree(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.CREATE_INDEX_BTREE
                cursor.execute(command)

    def create_index_age_hash(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.CREATE_INDEX_HASH
                cursor.execute(command)
