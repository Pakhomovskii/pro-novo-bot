import sqlite3

# Connect to the SQLite database

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

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
        pts TEXT,
        body_type TEXT,
        drive TEXT,
        engine_capacity TEXT,
        year TEXT,
        fuel_type TEXT,
        budget INTEGER,
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
