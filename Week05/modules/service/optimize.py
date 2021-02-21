from .queries import Queries


def check_performance(queries: Queries):
    print("Before applying indexes on attribute 'Age'.")
    queries.performance_select_adults_btree()
    queries.performance_select_adults_hash()
    print()
    print("Indexes for tables 'customer_btree', 'customer_hash' for queries 'SELECT * FROM customer_btree "
          "WHERE Age >= 18 and Age <= 30' and 'SELECT * FROM customer_hash WHERE Age >= 18 and Age <= 30' "
          "were created successfully.")
    queries.create_index_age_btree()
    queries.create_index_age_hash()
    print()
    print("After applying indexes on attribute 'Age'.")
    queries.performance_select_adults_btree()
    queries.performance_select_adults_hash()
