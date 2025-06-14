import psycopg2
from api.config import *
from datetime import datetime
import secrets
from dotenv import load_dotenv
import os
load_dotenv()


class SQLDatabase:
    def __init__(self):
        conn = psycopg2.connect(database=os.getenv("DATABASE"), host=os.getenv("HOST"), port=os.getenv("PORT"), user=os.getenv("USER"), password=os.getenv("PASSWORD"))
        self.cur = conn.cursor()
        conn.set_session(autocommit=True)

    def test_db(self):
        self.cur.execute(f"select age from customers where user_id = 'ad089c26-f733-4535-9901-bfbf827272b5'")
        return self.cur.fetchall()[0][0]

    def execute_query(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()


