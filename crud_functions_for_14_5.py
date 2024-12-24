import sqlite3
connection = sqlite3.connect("products.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    ); 
    ''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_title ON Products (title)")

cursor.execute('DELETE FROM Products')  # Очистка таблицы перед её заполнением


def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       (f"Продукт {i}", f"Описание {i}", f"{i * 100}"))
    connection.commit()


def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return products



connection = sqlite3.connect("usersbase.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INT NOT NULL,
balance INT NOT NULL
);
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_username ON Users (username)")

cursor.execute('DELETE FROM Users')     # Очистка таблицы перед её заполнением


def is_included(username):
    connection = sqlite3.connect("usersbase.db")
    cursor = connection.cursor()

    users_list = cursor.execute("SELECT username FROM Users").fetchall()
    connection.commit()
    return (username, ) in users_list


def add_user(username, email, age):
    connection = sqlite3.connect("usersbase.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
        (f'{username}', f'{email}', f'{age}', f'{1000}'))

    connection.commit()


connection.commit()
connection.close()
