import psycopg2
import sys


def connect(database='postgres', user="postgres", password="postgres", host="localhost", port="5432"):
    connection_db = None
    try:
        connection_db = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    except psycopg2.DatabaseError as ex:
        print('Unable connect to the database: ' + ex)
        sys.exit(1)
    print('Connection has been established.')
    return connection_db
