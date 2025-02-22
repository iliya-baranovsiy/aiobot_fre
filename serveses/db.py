import sqlite3


async def create_db():
    connection = sqlite3.connect('../bot_database.db')
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY,first_name TEXT,last_name TEXT)")
    connection.close()


async def create_record(id, d_name, l_name):
    connection = sqlite3.connect('../bot_database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT OR IGNORE INTO Users (id, first_name, last_name) VALUES (?, ?, ?)', (id, d_name, l_name))
    connection.commit()
    connection.close()


async def select():
    connection = sqlite3.connect('../bot_database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM Users")
    users_id = cursor.fetchall()
    user_list = []
    for user in users_id:
        user_list.append(user[0])
    connection.close()
    return user_list

