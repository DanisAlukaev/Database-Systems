from .queries import Queries


def _exercise1(queries: Queries):
    print('Exercise #1: ')
    print("Before applying indexes on attribute 'Age'.")
    queries.analyze_btree_age()
    queries.analyze_hash_age()
    print()
    print("Indexes for tables 'customer_btree', 'customer_hash' for queries 'SELECT * FROM customer_btree "
          "WHERE Age >= 18 and Age <= 30' and 'SELECT * FROM customer_hash WHERE Age >= 18 and Age <= 30' "
          "were created successfully.")
    queries.index_btree_age()
    queries.index_hash_age()
    print()
    print("After applying indexes on attribute 'Age'.")
    queries.analyze_btree_age()
    queries.analyze_hash_age()
    print()


def _exercise2(queries: Queries):
    print('Exercise #2: ')
    print("Before applying indexes on attribute 'name'.")
    queries.analyze_btree_name()
    queries.analyze_hash_name()
    print()
    print("Indexes for tables 'customer_btree', 'customer_hash' for queries 'SELECT * FROM customer_btree "
          "WHERE name ~ 'A.+'; and 'SELECT * FROM customer_hash WHERE name ~ 'A.+'; were created successfully.")
    queries.index_btree_name()
    queries.index_hash_name()
    print()
    print("After applying indexes on attribute 'Name'.")
    queries.analyze_btree_name()
    queries.analyze_hash_name()
    print()


def check_performance(queries: Queries):
    _exercise1(queries)
    _exercise2(queries)
