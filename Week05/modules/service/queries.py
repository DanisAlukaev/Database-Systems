class Queries:
    SELECT_ALL_CUSTOMER1 = "SELECT * FROM customer1;"
    SELECT_ALL_CUSTOMER2 = "SELECT * FROM customer2;"

    ADD_CUSTOMER_CUSTOMER1 = "INSERT INTO customer1(name, address, age, review) VALUES (%s, %s, %s, %s);"
    ADD_CUSTOMER_CUSTOMER2 = "INSERT INTO customer2(name, address, age, review) VALUES (%s, %s, %s, %s);"

    INDEX_BTREE_CUSTOMER1 = "CREATE INDEX btree_ex1 ON customer1 USING BTREE (age);"
    INDEX_HASH_CUSTOMER2 = "CREATE INDEX hash_ex1 ON customer2 USING HASH (age);"
    INDEX_GIN_CUSTOMER1 = "CREATE INDEX gin_ex2 ON customer1 USING GIN (to_tsvector('english', review));"
    INDEX_GIST_CUSTOMER2 = "CREATE INDEX gist_ex2 ON customer2 USING GIST (to_tsvector('english', review));"

    ANALYZE_EXERCISE1_CUSTOMER1 = "EXPLAIN ANALYZE SELECT * FROM customer1 WHERE age >= 18 AND age <= 22;"
    ANALYZE_EXERCISE1_CUSTOMER2 = "EXPLAIN ANALYZE SELECT * FROM customer2 WHERE age >= 18 AND age <= 22;"
    ANALYZE_EXERCISE2_CUSTOMER1 = "EXPLAIN ANALYZE SELECT * FROM customer1 WHERE to_tsvector('english', review) @@ to_tsquery('english', 'media | conference | camera | economic | company | cost');"
    ANALYZE_EXERCISE2_CUSTOMER2 = "EXPLAIN ANALYZE SELECT * FROM customer2 WHERE to_tsvector('english', review) @@ to_tsquery('english', 'media | conference | camera | economic | company | cost');"

    def __init__(self, connection_db):
        self.connection_db = connection_db

    def create_tables(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                create_query = open("./modules/service/database.sql", "r").read()
                cursor.execute(create_query)

    def select_all_customer1(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.SELECT_ALL_CUSTOMER1
                cursor.execute(command)

    def select_all_customer2(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.SELECT_ALL_CUSTOMER2
                cursor.execute(command)

    def add_customer_customer1(self, name, address, age, review):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ADD_CUSTOMER_CUSTOMER1
                args = name, address, age, review
                cursor.execute(command, args)

    def add_customer_customer2(self, name, address, age, review):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ADD_CUSTOMER_CUSTOMER2
                args = name, address, age, review
                cursor.execute(command, args)

    def index_btree_customer1(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.INDEX_BTREE_CUSTOMER1
                cursor.execute(command)

    def index_hash_customer2(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.INDEX_HASH_CUSTOMER2
                cursor.execute(command)

    def index_gin_customer1(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.INDEX_GIN_CUSTOMER1
                cursor.execute(command)

    def index_gist_customer2(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.INDEX_GIST_CUSTOMER2
                cursor.execute(command)

    def analyze_exercise1_customer1(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ANALYZE_EXERCISE1_CUSTOMER1
                cursor.execute(command)
                return cursor.fetchall()

    def analyze_exercise1_customer2(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ANALYZE_EXERCISE1_CUSTOMER2
                cursor.execute(command)
                return cursor.fetchall()

    def analyze_exercise2_customer1(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ANALYZE_EXERCISE2_CUSTOMER1
                cursor.execute(command)
                return cursor.fetchall()

    def analyze_exercise2_customer2(self):
        with self.connection_db:
            with self.connection_db.cursor() as cursor:
                command = self.ANALYZE_EXERCISE2_CUSTOMER2
                cursor.execute(command)
                return cursor.fetchall()
