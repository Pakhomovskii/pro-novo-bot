import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


async def get_user_order(user_chat_id):
    conn.execute('BEGIN')
    cursor.execute('''
            SELECT brand, model, pts, body_type, drive, engine_capacity, year, fuel_type, budget FROM orders
            WHERE user_id=?''', (user_chat_id,))
    # Fetch all the rows
    order = cursor.fetchall()
    conn.commit()
    if order is None:
        return []
    return order


async def create_user(user_chat_id, user_name, user_first_name):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
               INSERT INTO users (user_chat_id, user_name, user_first_name)
               VALUES (?, ?, ?);
           ''', (user_chat_id, user_name, user_first_name))

        cursor.execute('''
            INSERT INTO orders (brand, model, pts, body_type, drive, engine_capacity, year, fuel_type, budget, user_id)
            VALUES ('','','','','','','','',0, ?)
        ''', (user_chat_id,))

        cursor.execute('''
                    INSERT INTO temporary_budget (budget, user_id)
                    VALUES (0, ?)
                ''', (user_chat_id,))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def update_user_order_brand(brand=None, user_chat_id=None):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE orders
            SET brand=?
            WHERE user_id = ?
        ''', (brand, user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def update_user_order_model(model=None, user_chat_id=None):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE orders
            SET model=?
            WHERE user_id = ?
        ''', (model, user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def delete_user_order(brand="", model="", pts="", body_type="",
                            drive="", engine_capacity="", year="",
                            fuel_type="", budget="", user_chat_id=None):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE orders
            SET brand=?, model=?, pts=?, body_type=?, drive=?, engine_capacity=?, year=?, fuel_type=?, budget=?
            WHERE user_id = ?
        ''', (brand, model, pts, body_type, drive, engine_capacity, year, fuel_type, budget, user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def show_temporary_budget(user_chat_id):
    conn.execute('BEGIN')
    cursor.execute('''
            SELECT budget FROM temporary_budget
            WHERE user_id=?''', (user_chat_id,))
    # Fetch all the rows
    order = cursor.fetchall()
    conn.commit()
    if order is None:
        return []
    return order


async def edit_temporary_budget(user_chat_id, value):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE temporary_budget
            SET budget=?
            WHERE user_id = ?
        ''', (value, user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def delete_user_temporary_budget(user_chat_id):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            DELETE FROM temporary_budget
            WHERE user_id = ?
        ''', (user_chat_id,))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()
