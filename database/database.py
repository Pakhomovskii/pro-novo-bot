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
    conn = psycopg2.connect(
        host="209.38.224.54",
        port=5432,
        database="pro-novo-bot",
        user="postgres",
        password="411652"
    )
    cursor = conn.cursor()


async def get_user_id_from_db(user_chat_id) -> bool:
    conn.execute('BEGIN')
    cursor.execute('''
            SELECT user_chat_id FROM users
            WHERE user_chat_id=?''', (user_chat_id,))
    # Fetch all the rows
    order = cursor.fetchall()
    conn.commit()
    if order:
        return True
    return False


async def get_user_order(user_chat_id):
    conn.execute('BEGIN')
    cursor.execute('''
            SELECT brand, model, hand_drive, power, drive, engine_capacity, year, fuel_type, budget FROM orders
            WHERE user_id=?''', (user_chat_id,))
    # Fetch all the rows
    order = cursor.fetchall()
    conn.commit()
    if order is None:
        return []
    return order


async def get_user_brand(user_chat_id):
    conn.execute('BEGIN')
    cursor.execute('''
            SELECT brand FROM orders
            WHERE user_id=?''', (user_chat_id,))
    # Fetch all the rows
    order = cursor.fetchall()
    conn.commit()
    if order is None:
        return []
    return order


async def get_user_contact(user_chat_id):
    conn.execute('BEGIN')
    cursor.execute('''
            SELECT user_name FROM users
            WHERE user_chat_id=?''', (user_chat_id,))
    # Fetch all the rows
    order = cursor.fetchall()
    conn.commit()
    if order is None:
        return []
    return order


async def get_user_budget(user_chat_id):
    conn.execute('BEGIN')
    cursor.execute('''
            SELECT budget  FROM orders
            WHERE user_id=?''', (user_chat_id,))
    # Fetch all the rows
    order = cursor.fetchall()
    conn.commit()
    if order is None:
        return []
    return order


async def get_user_power(user_chat_id):
    conn.execute('BEGIN')
    cursor.execute('''
            SELECT power  FROM orders
            WHERE user_id=?''', (user_chat_id,))
    # Fetch all the rows
    order = cursor.fetchall()
    conn.commit()
    if order is None:
        return []
    return order


async def get_user_fuel_type(user_chat_id):
    conn.execute('BEGIN')
    cursor.execute('''
            SELECT fuel_type  FROM orders
            WHERE user_id=?''', (user_chat_id,))
    # Fetch all the rows
    order = cursor.fetchall()
    conn.commit()
    if order is None:
        return []
    return order


async def get_user_car_age(user_chat_id):
    conn.execute('BEGIN')
    cursor.execute('''
            SELECT year FROM orders
            WHERE user_id=?''', (user_chat_id,))
    # Fetch all the rows
    order = cursor.fetchall()
    conn.commit()
    if order is None:
        return []
    return order


async def get_user_car_engine_capacity(user_chat_id):
    conn.execute('BEGIN')
    cursor.execute('''
            SELECT engine_capacity FROM orders
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
            INSERT INTO orders (brand, model, hand_drive, power, drive, engine_capacity, year, fuel_type, budget, user_id)
            VALUES ('','','','','','','','','', ?)
        ''', (user_chat_id,))

        cursor.execute('''
                    INSERT INTO temporary_budget (budget, user_id)
                    VALUES ('', ?)
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


async def update_user_order_engine_capacity(engine_capacity=None, user_chat_id=None):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE orders
            SET engine_capacity=?
            WHERE user_id = ?
        ''', (engine_capacity, user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def update_user_order_budget(budget=None, user_chat_id=None):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE orders
            SET budget=?
            WHERE user_id = ?
        ''', (budget, user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def update_user_order_hand_drive(hand_drive=None, user_chat_id=None):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE orders
            SET hand_drive=?
            WHERE user_id = ?
        ''', (hand_drive, user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def update_user_order_year(year=None, user_chat_id=None):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE orders
            SET year=?
            WHERE user_id = ?
        ''', (year, user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def update_user_order_drive(drive=None, user_chat_id=None):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE orders
            SET drive=?
            WHERE user_id = ?
        ''', (drive, user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def update_user_order_fuel(fuel_type=None, user_chat_id=None):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE orders
            SET fuel_type=?
            WHERE user_id = ?
        ''', (fuel_type, user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def update_user_order_power(power=None, user_chat_id=None):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE orders
            SET power=?
            WHERE user_id = ?
        ''', (power, user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def delete_user_order(brand='', model='', hand_drive='', power='',
                            drive='', engine_capacity='', year='',
                            fuel_type='', budget='', user_chat_id=None):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE orders
            SET brand=?,
             model=?, 
             hand_drive=?, 
             power=?, 
             drive=?, 
             engine_capacity=?,
              year=?,
               fuel_type=?,
                budget=?
            WHERE user_id = ?   
        ''', (brand,
              model,
              hand_drive,
              power,
              drive,
              engine_capacity,
              year,
              fuel_type,
              budget,
              user_chat_id))
        conn.commit()
    except sqlite3.Error:
        print(sqlite3.Error)
        conn.rollback()


async def delete_user_model(user_chat_id=None):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE orders
            SET model=?
            WHERE user_id = ?
        ''', ("", user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def delete_user_temporary_budget(user_chat_id):
    try:
        conn.execute('BEGIN')
        cursor.execute('''
            UPDATE temporary_budget
            SET budget=?
            WHERE user_id = ? and budget <> '';
        ''', ('', user_chat_id))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()


async def show_temporary_budget(user_chat_id):
    conn.execute('BEGIN')
    cursor.execute('''
            SELECT budget FROM temporary_budget
            WHERE user_id=?''', (user_chat_id,))
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


