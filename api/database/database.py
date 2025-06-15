import psycopg2
from api.config import *
from datetime import datetime
import secrets
from dotenv import load_dotenv
import os
load_dotenv()


class SQLDatabase:
    def __init__(self):
        conn = psycopg2.connect(
            database=os.getenv("DATABASE"),
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("PASSWORD"),
        )
        self.cur = conn.cursor()
        conn.set_session(autocommit=True)

    def test_db(self):
        self.cur.execute(f"select age from customers where user_id = 'ad089c26-f733-4535-9901-bfbf827272b5'")
        return self.cur.fetchall()[0][0]

    def execute_query(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def insert_transfer_money_history(self, receiver, note, amount):
        transaction_id = "tx_" + datetime.now().strftime("%Y%m%d%H%m") + secrets.token_hex(3)
        receiver_card_id = "TCB_"+receiver
        query = """INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount)
VALUES (%s, 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', %s, %s, %s, %s);
"""
        self.cur.execute(query, (transaction_id, receiver_card_id, receiver, note, amount))

    def get_transaction_history(self):
        self.cur.execute(f"select sender_name, receiver_name, amount, note, created_at from transaction_history")
        return self.cur.fetchall()


