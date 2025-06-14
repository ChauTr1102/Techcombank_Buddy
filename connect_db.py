import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DATABASE")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
print(DB_USER, DB_NAME, PASSWORD, HOST, PORT)
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
def test_connection():
    try:
        conn = psycopg2.connect(
            user=DB_USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DB_NAME
        )
        print("✅ Connected successfully to PostgreSQL!")
        cur = conn.cursor()
        cur.execute("SELECT version();")
        print("PostgreSQL version:", cur.fetchone())
        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Connection failed:", e)


print(HOST, PORT, DB_USER, PASSWORD, DB_NAME)
test_connection()
