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
        self.cur.execute(f"select age from customers where user_id = 'ad089c26-f733-4535-9901-bfbf827272b5'")
        return self.cur.fetchall()[0][0]

