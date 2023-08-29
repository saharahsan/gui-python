import sqlite3
     
def create_table():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS Bill (
            id TEXT,
            name TEXT,
            date TEXT,
            catogry TEXT,
            item TEXT,
            price INT,
            quantity INT
             )''')
    
    conn.commit()
    conn.close()

def fetch_item():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Bill')
    Products = cursor.fetchall()
    conn.close()
   
    return Products

def update_stocks(item, quantity):
    with sqlite3.connect('Products.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE Products SET in_stock = in_stock - ? WHERE name = ? RETURNING in_stock', (quantity, item))
        updated_stocks = cursor.fetchone()
        
        return updated_stocks # return the new stock value
    
def insert_product(id, customer_name, date, catogry, item, price,quantity):
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO Bill (id, name, date, catogry, item, price, quantity) VALUES (?, ?, ?, ?, ?, ?, ?)',
                   (id, customer_name, date, catogry, item, price, quantity)) 
    conn.commit()
    conn.close()
    
def delete_product(price,id,quantity):
    conn = sqlite3.connect('Products.db')
    cursor =conn.cursor()
    cursor.execute('DELETE FROM Bill WHERE price= ? AND id = ? AND quantity = ?', (price,id,quantity))
    
    conn.commit()
    conn.close()

def udelete_stocks(item, quantity):
    with sqlite3.connect('Products.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE Products SET in_stock = in_stock + ? WHERE name = ? RETURNING in_stock ', (quantity, item))
        i=cursor.fetchone()
        return i
    
    

def fetch_all_item():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM Products')
    item = cursor.fetchall()
    conn.close()
    return [i[0] for i in item]

def fetch_all_catogry():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT catogry FROM Products')
    catogry = cursor.fetchall()
    conn.close()
    return [i[0] for i in catogry]

def fetch_all_ids():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT id FROM Bill')
    ids = cursor.fetchall()
    conn.close()
    return [i[0] for i in ids]

def fetch_price(item):
    conn = sqlite3.connect('Products.db',detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    cursor.execute('SELECT sale_price FROM Products WHERE name = ? ',(item,))
    price = cursor.fetchone()
    
    return price
    
    
create_table()