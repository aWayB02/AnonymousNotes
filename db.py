import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def db_connect():
    conn = psycopg2.connect(
        dbname=os.environ.get("DBNAME"),
        user=os.environ.get("USER"),
        password=os.environ.get("PASSWORD")
    )

    return conn

def create_table():
    
    conn = db_connect()
    cur = conn.cursor()

    cur.execute(""" 
        CREATE TABLE notes
        (
            id SERIAL PRIMARY KEY,
            unique_id UUID,
            note TEXT,
            timer timestamp,
            password TEXT
        )
        """)
    
    conn.commit()
    conn.close()