import os

class Queries:
    SELECT_ALL_BTREE = "SELECT * FROM customer_btree"
    SELECT_ALL_HASH = "SELECT * FROM customer_hash"
    ADD_CUSTOMER_BTREE = "INSERT INTO customer_btree(Name, Address, Review) VALUES (%s, %s, %s);"
    ADD_CUSTOMER_HASH = "INSERT INTO customer_hash(Name, Address, Review) VALUES (%s, %s, %s);"
    CREATE_INDEX_BTREE = ""
    CREATE_INDEX_HASH = ""
    ANALYZE_BTREE = ""
    ANALYZE_HASH = ""

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

    def add_customer_btree(self, name, address, review):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ADD_CUSTOMER_BTREE
                args = name, address, review
                cursor.execute(command, args)

    def add_customer_hash(self, name, address, review):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ADD_CUSTOMER_HASH
                args = name, address, review
                cursor.execute(command, args)
