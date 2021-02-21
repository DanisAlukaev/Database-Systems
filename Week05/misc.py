from modules.database import create
from config import PG_DB, PG_USER, PG_PASS, PG_HOST, PG_PORT
from modules.service.queries import Queries

connection_db = create.connect(database=PG_DB, user=PG_USER, password=PG_PASS, host=PG_HOST, port=PG_PORT)
queries = Queries(connection_db)
