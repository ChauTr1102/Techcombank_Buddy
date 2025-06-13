import psycopg2
from api.config import *
from datetime import datetime
import secrets


class SQLDatabase:
    def __init__(self):
        conn = psycopg2.connect(database=DATABASE, host=HOST, port=PORT, user=USER, password=PASSWORD)
        self.cur = conn.cursor()
        conn.set_session(autocommit=True)

    def test_db(self):
        self.cur.execute(f"select * from customers")
        return self.cur.fetchall()

