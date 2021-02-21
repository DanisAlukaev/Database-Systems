from faker import Faker
from .queries import Queries
from random import randint


def init_tables(queries: Queries):
    queries.create_tables()
    print("Tables 'customer_btree', 'customer_hash' were created successfully.")


def populate(queries: Queries):
    fake = Faker()
    print('Populating...')
    for i in range(100000):
        if i % 10000 == 0 and i > 0:
            print('Created {} customers.'.format(i))
        data = fake.name(), fake.address(), randint(14, 80), fake.text()
        queries.add_customer_btree(*data)
        queries.add_customer_hash(*data)
    print('Done!')
