import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS model_users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY, name text, price int)"
cursor.execute(create_table)


connection.commit()

connection.close()	