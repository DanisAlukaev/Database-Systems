from faker import Faker
from .queries import Queries


def init_tables(queries: Queries):
    queries.create_tables()
    print("Tables 'customer_btree', 'customer_hash' were created successfully.")


def populate(queries: Queries):
    fake = Faker()
    for i in range(10):
        data = fake.name(), fake.address(), fake.text()
        queries.add_customer_btree(*data)
        queries.add_customer_hash(*data)
