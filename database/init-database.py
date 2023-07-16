import os
import sqlite3

import psycopg2

try:
    DEBUG = os.environ.get('DEBUG')
except:
    DEBUG = "0"

if DEBUG == "1":
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

else:
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password="411652"
    )
    cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_chat_id INTEGER PRIMARY KEY,
        user_name TEXT,
        user_first_name TEXT)
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        model TEXT,
        hand_drive TEXT,
        power TEXT,
        drive TEXT,
        engine_capacity TEXT,
        year TEXT,
        fuel_type TEXT,
        budget TEXT,
        user_id INTEGER UNIQUE,
        FOREIGN KEY (user_id) REFERENCES users(user_chat_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS temporary_budget (
        id INTEGER PRIMARY KEY,
        budget TEXT,
        user_id INTEGER UNIQUE,
        FOREIGN KEY (user_id) REFERENCES users(user_chat_id)
    )
''')

conn.commit()
conn.close()
