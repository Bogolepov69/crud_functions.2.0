import sqlite3

class Products:
    def __init__(self):
        self.data = [
            ('1', 'Product1', 'Описание первого товара', 100),
            ('2', 'Product2', 'Описание второго товара', 200),
            ('3', 'Product3', 'Описание третьего товара', 300),
            ('4', 'Product4', 'Описание четвертого товара', 400)
        ]

def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )''')
    for product in Products().data:
        cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)", product)
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

class Users:
    def __init__(self):
        self.data = [
            ('1', 'user1', '1@mail.ru', 25, 1000),
            ('2', 'user2', '2@mail.ru', 30, 1000),
            ('3', 'user3', '3@mail.ru', 35, 1000),
            ('4', 'user4', '4@mail.ru', 40, 1000)
        ]

def initiate_db_users():
    conn = sqlite3.connect('Users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )''')
    for user in Users().data:
        cursor.execute("INSERT INTO Users (id, username, email, age, balance) VALUES (?, ?, ?, ?, ?)", user)
    conn.commit()
    conn.close()

def add_user(username, email, age):
    conn = sqlite3.connect('Users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (username, email, age, 1000))
    conn.commit()
    conn.close()

def is_included(username):
    conn = sqlite3.connect('Users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

initiate_db_users()