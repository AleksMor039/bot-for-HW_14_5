'''черновик БД для бота модуля 14_5'''

import sqlite3

'''ф-ия созд. табл. Products и табл. Users'''


def initiate_db():
    connection = sqlite3.connect("prod_dtb.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INT NOT NULL
     );
    ''')
    connection.commit()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL
         );
        ''')
    connection.commit()
    connection.close()


'''ф-ия возвр. записи из таблицы Products'''


def get_all_products():
    connection = sqlite3.connect("prod_dtb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, description, price FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products


'''ф-ия добавляет запись в таблицу Products'''


def add_bd(id, title, description, price):
    connection = sqlite3.connect("prod_dtb.db")
    cursor = connection.cursor()
    # проверка сущ. запись с таким id
    cursor.execute("SELECT * FROM Products WHERE id=?", (id,))
    if cursor.fetchone() is None:  # если записи нет, добавляем её
        cursor.execute(
            "INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)",
            (id, title, description, price))
        connection.commit()
        print(f"Продукт с id={id} успешно добавлен.")
    else:
        print(f"Продукт с id={id} уже существует.")
    connection.close()


'''ф-ия добавляет запись в таблицу Users'''


def add_user(username, email, age):
    connection = sqlite3.connect("prod_dtb.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', age, 1000))
    connection.commit()
    connection.close()


'''ф-ия проверки пользователя'''


def is_included(username):
    connection = sqlite3.connect("prod_dtb.db")
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check_user.fetchone() is None:
        return True
    else:
        return False
    connection.commit()
    connection.close()
