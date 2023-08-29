import sqlite3
     
def create_table():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS Products (
            id TEXT PRIMARY KEY,
            name TEXT,
            catogry TEXT,
            in_stock INTEGER,
            price INTEGER,
            sale_price INTEGER,
            date TEXT )''')
    conn.commit()
    conn.close()

def fetch_products():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    Products = cursor.fetchall()
    conn.close()
    return Products
def insert_product(id, name, catogry, in_stock, price,sale_price,date):
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Products (id, name, catogry, in_stock, price,sale_price,date) VALUES (?, ?, ?, ?, ?, ?, ?)',
                   (id, name, catogry, in_stock, price,sale_price,date))
    conn.commit()
    conn.close()
def delete_product(id):
    conn = sqlite3.connect('Products.db')
    cursor =conn.cursor()
    cursor.execute('DELETE FROM Products WHERE id = ?', (id,))
    conn.commit()
    conn.close()
def update_product(new_name, new_catogry, new_stock,new_price,new_sale_price,new_date, id):
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Products SET name = ?, catogry = ?, in_stock = ?, price = ?,sale_price = ?, date = ? WHERE id = ?",
                  (new_name, new_catogry, new_stock, new_price,new_sale_price,new_date, id) )
    conn.commit()
    conn.close()
def id_exists(id):
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Products WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0
def search_product_id(query):
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * From Products WHERE id = ?',(query,))
    row = cursor.fetchone()
    conn.close()
    return row

def search_product_name(query):
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * From Products WHERE name = ?',(query,))
    row = cursor.fetchone()
    conn.close()
    return row

def fetch_all_ids():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM Products')
    ids = cursor.fetchall()
    conn.close()
    return [i[0] for i in ids]

def fetch_all_item():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM Products')
    item = cursor.fetchall()
    conn.close()
    return [i[0] for i in item]

create_table()

    