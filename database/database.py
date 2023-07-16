import psycopg2

conn = psycopg2.connect(
    host="209.38.224.54",
    port=5432,
    database="pro-novo-bot",
    user="postgres",
    password="411652"
)
cursor = conn.cursor()


async def get_user_id_from_db(user_chat_id) -> bool:
    cursor.execute('''
        SELECT user_chat_id FROM users
        WHERE user_chat_id = %s
    ''', (user_chat_id,))
    # Fetch the row
    order = cursor.fetchone()
    if order:
        return True
    return False


async def get_user_order(user_chat_id):
    cursor.execute('''
        SELECT brand, model, hand_drive, power, drive, engine_capacity, year, fuel_type, budget
        FROM orders
        WHERE user_id = %s
    ''', (user_chat_id,))
    # Fetch the row
    order = cursor.fetchone()
    if order is None:
        return []
    return order


async def get_user_brand(user_chat_id):
    cursor.execute('''
        SELECT brand FROM orders
        WHERE user_id = %s
    ''', (user_chat_id,))
    # Fetch the row
    order = cursor.fetchone()
    if order is None:
        return []
    return order


# ... (similarly rewrite other functions)


async def get_user_contact(user_chat_id):
    cursor.execute('''
        SELECT user_name FROM orders
        WHERE user_id = %s
    ''', (user_chat_id,))
    # Fetch the row
    order = cursor.fetchone()
    if order is None:
        return []
    return order


async def get_user_budget(user_chat_id):
    cursor.execute('''
        SELECT budget FROM orders
        WHERE user_id = %s
    ''', (user_chat_id,))
    # Fetch the row
    order = cursor.fetchone()
    if order is None:
        return []
    return order


async def get_user_power(user_chat_id):
    cursor.execute('''
        SELECT power FROM orders
        WHERE user_id = %s
    ''', (user_chat_id,))
    # Fetch the row
    order = cursor.fetchone()
    if order is None:
        return []
    return order


async def get_user_fuel_type(user_chat_id):
    cursor.execute('''
        SELECT fuel_type FROM orders
        WHERE user_id = %s
    ''', (user_chat_id,))
    # Fetch the row
    order = cursor.fetchone()
    if order is None:
        return []
    return order


async def get_user_car_age(user_chat_id):
    cursor.execute('''
        SELECT year FROM orders
        WHERE user_id = %s
    ''', (user_chat_id,))
    # Fetch the row
    order = cursor.fetchone()
    if order is None:
        return []
    return order

async def get_user_car_engine_capacity(user_chat_id):
    cursor.execute('''
        SELECT engine_capacity FROM orders
        WHERE user_id = %s
    ''', (user_chat_id,))
    # Fetch the row
    order = cursor.fetchone()
    if order is None:
        return []
    return order


async def create_user(user_chat_id, user_name, user_first_name):
    try:
        cursor.execute('''
            INSERT INTO users (user_chat_id, user_name, user_first_name)
            VALUES (%s, %s, %s)
        ''', (user_chat_id, user_name, user_first_name))

        cursor.execute('''
            INSERT INTO orders (brand, model, hand_drive, power, drive, engine_capacity, year, fuel_type, budget, user_id)
            VALUES ('', '', '', '', '', '', '', '', '', %s)
        ''', (user_chat_id,))

        cursor.execute('''
            INSERT INTO temporary_budget (budget, user_id)
            VALUES ('', %s)
        ''', (user_chat_id,))
        conn.commit()
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()


# ... (similarly rewrite other functions)
async def update_user_order_brand(brand=None, user_chat_id=None):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE orders
            SET brand=$1
            WHERE user_id=$2
        '''
        await conn.execute(update_query, brand, user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")

async def update_user_order_model(model=None, user_chat_id=None):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE orders
            SET model=$1
            WHERE user_id=$2
        '''
        await conn.execute(update_query, model, user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")

async def update_user_order_engine_capacity(engine_capacity=None, user_chat_id=None):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE orders
            SET engine_capacity=$1
            WHERE user_id=$2
        '''
        await conn.execute(update_query, engine_capacity, user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")

async def update_user_order_budget(budget=None, user_chat_id=None):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE orders
            SET budget=$1
            WHERE user_id=$2
        '''
        await conn.execute(update_query, budget, user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")


async def update_user_order_hand_drive(hand_drive=None, user_chat_id=None):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE orders
            SET hand_drive=$1
            WHERE user_id=$2
        '''
        await conn.execute(update_query, hand_drive, user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")


async def update_user_order_year(year=None, user_chat_id=None):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE orders
            SET year=$1
            WHERE user_id=$2
        '''
        await conn.execute(update_query, year, user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")


async def update_user_order_drive(drive=None, user_chat_id=None):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE orders
            SET drive=$1
            WHERE user_id=$2
        '''
        await conn.execute(update_query, drive, user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")


async def update_user_order_fuel(fuel_type=None, user_chat_id=None):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE orders
            SET fuel_type=$1
            WHERE user_id=$2
        '''
        await conn.execute(update_query, fuel_type, user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")


async def update_user_order_power(power=None, user_chat_id=None):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE orders
            SET power=$1
            WHERE user_id=$2
        '''
        await conn.execute(update_query, power, user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")


import asyncpg


async def delete_user_order(brand='', model='', hand_drive='', power='',
                            drive='', engine_capacity='', year='',
                            fuel_type='', budget='', user_chat_id=None):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE orders
            SET brand=$1,
             model=$2, 
             hand_drive=$3, 
             power=$4, 
             drive=$5, 
             engine_capacity=$6,
              year=$7,
               fuel_type=$8,
                budget=$9
            WHERE user_id=$10
        '''
        await conn.execute(update_query, brand, model, hand_drive, power,
                           drive, engine_capacity, year, fuel_type, budget, user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")

async def delete_user_model(user_chat_id=None):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE orders
            SET model=$1
            WHERE user_id=$2
        '''
        await conn.execute(update_query, "", user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")

async def delete_user_temporary_budget(user_chat_id):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE temporary_budget
            SET budget=$1
            WHERE user_id=$2 and budget <> '';
        '''
        await conn.execute(update_query, "", user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")


async def show_temporary_budget(user_chat_id):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        select_query = '''
            SELECT budget FROM temporary_budget
            WHERE user_id=$1
        '''
        result = await conn.fetch(select_query, user_chat_id)

        await conn.close()
        return result

    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")

async def edit_temporary_budget(user_chat_id, value):
    try:
        conn = await asyncpg.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        update_query = '''
            UPDATE temporary_budget
            SET budget=$1
            WHERE user_id=$2
        '''
        await conn.execute(update_query, value, user_chat_id)

        await conn.close()
        print("Update successful!")
    except asyncpg.PostgresError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    conn.close()
