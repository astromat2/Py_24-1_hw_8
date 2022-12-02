import sqlite3

def create_connection(products):
    conn = None
    try:
        conn = sqlite3.connect(products)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_product(conn, products: tuple):
    try:
        sql = '''
        INSERT INTO  products(product_title, price, quantity)
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def create_products(conn):
    create_product(conn, ('Cola', 14.5, 14))
    create_product(conn, ('Fanta', 37.5, 14))
    create_product(conn, ('BenQ', 12.5, 13))
    create_product(conn, ('Pepsi', 41.5, 54))
    create_product(conn, ('Apple', 12.3, 19))
    create_product(conn, ('Xiaomi', 37.5, 51))
    create_product(conn, ('Samsung', 47.5, 18))
    create_product(conn, ('Sprite', 17.5, 57))
    create_product(conn, ('HP', 37.5, 34))
    create_product(conn, ('Lacoste', 67.5, 34))
    create_product(conn, ('Vivo', 27.5, 12))
    create_product(conn, ('Nvidia', 67.5, 14))
    create_product(conn, ('IKEA', 37.5, 54))
    create_product(conn, ('Acer', 37.5, 44))
    create_product(conn, ('Asus', 67.5, 24))


def update_price(conn, products):
    try:
        sql = '''
        UPDATE products SET price = ? WHERE id = ?
        '''
        curcor = conn.cursor()
        curcor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def delete_id(conn, id):
    try:
        sql = '''
        DELETE FROM products WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, id)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
    return conn


def choise_products(conn):
    try:
        sql = '''
        SELECT * FROM products WHERE price < 100 AND quantity > 5
        '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
    return []


def search_products(conn, word):
    try:
        sql = '''
        SELECT * FROM products WHERE product_title LIKE ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
    return conn


def update_products_quantity(conn, products):
    try:
        sql = '''
        UPDATE products SET quantity = ? WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


database = r'hw.db'
sql_create_products_table = '''
CREATE TABLE products ( 
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
quantity INT(5) NOT NULL DEFAULT 0
)
'''
connection = create_connection(database)
if connection is not None:
    print('Ready.')
    create_table(connection, sql_create_products_table)
    # create_products(connection)
    update_products_quantity(connection,(5,1))
    print('---------------------------------------')
    update_price(connection, (39.70, 2))
    print('---------------------------------------')
    delete_id(connection, (1,))
    select_all_products(connection)
    print('---------------------------------------')
    choise_products(connection)
    print('---------------------------------------')
    search_products(connection, 'Apple')

