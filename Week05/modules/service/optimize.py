from .queries import Queries


def _exercise1(queries: Queries):
    print('\nExercise #1: ')
    print("Before applying indexes.")
    tables = queries.analyze_exercise1_customer1(), queries.analyze_exercise1_customer2()
    print("Table 'customer1': ", tables[0])
    print("Table 'customer2': ", tables[1])

    print("Indexes for tables 'customer1' (B-tree), 'customer2' (Hash) were created successfully.")
    queries.index_btree_customer1()
    queries.index_hash_customer2()

    print("After applying indexes.")
    tables = queries.analyze_exercise1_customer1(), queries.analyze_exercise1_customer2()
    print("Table 'customer1': ", tables[0])
    print("Table 'customer2': ", tables[1])


def _exercise2(queries: Queries):
    print('\nExercise #2: ')

    print("Before applying indexes.")
    tables = queries.analyze_exercise2_customer1(), queries.analyze_exercise2_customer2()
    print("Table 'customer1': ", tables[0])
    print("Table 'customer2': ", tables[1])

    print("Indexes for tables 'customer1' (GIN), 'customer2' (GiST) were created successfully.")
    queries.index_gin_customer1()
    queries.index_gist_customer2()

    print("After applying indexes.")
    tables = queries.analyze_exercise2_customer1(), queries.analyze_exercise2_customer2()
    print("Table 'customer1': ", tables[0])
    print("Table 'customer2': ", tables[1])


def check_performance(queries: Queries):
    _exercise1(queries)
    _exercise2(queries)
