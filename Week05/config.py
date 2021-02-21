import os
from dotenv import load_dotenv

load_dotenv()

PG_HOST = os.getenv("PG_HOST")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
PG_DB = os.getenv("PG_DB")
PG_PORT = os.getenv("PG_PORT")
