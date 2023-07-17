import asyncpg as ap

async def create_tables():
    try:
        conn = await ap.connect(
            host="209.38.224.54",
            port=5432,
            database="pro-novo-bot",
            user="postgres",
            password="411652"
        )

        create_users_table = '''
            CREATE TABLE IF NOT EXISTS users (
                user_chat_id BIGINT PRIMARY KEY,
                user_name TEXT,
                user_first_name TEXT
            )
        '''

        create_orders_table = '''
            CREATE TABLE IF NOT EXISTS orders (
                id SERIAL PRIMARY KEY,
                brand TEXT,
                model TEXT,
                hand_drive TEXT,
                power TEXT,
                drive TEXT,
                engine_capacity TEXT,
                year TEXT,
                fuel_type TEXT,
                budget TEXT,
                user_id BIGINT UNIQUE,
                FOREIGN KEY (user_id) REFERENCES users(user_chat_id)
            )
        '''

        create_temporary_budget_table = '''
            CREATE TABLE IF NOT EXISTS temporary_budget (
                id SERIAL PRIMARY KEY,
                budget TEXT,
                user_id BIGINT UNIQUE,
                FOREIGN KEY (user_id) REFERENCES users(user_chat_id)
            )
        '''

        await conn.execute(create_users_table)
        await conn.execute(create_orders_table)
        await conn.execute(create_temporary_budget_table)

        await conn.close()
        print("Tables created successfully!")
    except ap.PostgresError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    import asyncio

    asyncio.get_event_loop().run_until_complete(create_tables())
