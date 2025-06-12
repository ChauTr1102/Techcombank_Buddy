import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.getenv("DATABASE")
HOST=os.getenv("HOST")
PORT=os.getenv("PORT")
USER=os.getenv("USER")
PASSWORD=os.getenv("PASSWORD")
DB_NAME=os.getenv("DB_NAME")

def test_connection():
    try:
        conn = psycopg2.connect(
            user=USER,
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


print(HOST, PORT, USER, PASSWORD, DB_NAME)
test_connection()
