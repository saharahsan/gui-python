import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from datetime import date
import database2
import sqlite3


app = customtkinter.CTk()
app.geometry('1300x700')
app.title('Billing Software')
app.config(bg='plum')
app.resizable(False,False)

font1 =('Arial',25,'bold')
font2 =('Arial',18,'bold')
font3 =('Arial',13,'bold')

def insert_item_options():
    item = database2.fetch_all_item()
    item_options.configure(values=item)

def catogry_item_options():
    catogry = database2.fetch_all_catogry()
    category_options.configure(values=catogry)
    
def insert_ids_options():
    ids = database2.fetch_all_ids()
    select_options.configure(values=ids)
    

def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        id_entry.insert(0,row[0])
        name_entry.insert(0,row[1])
        category_options.set('Select')
        item_options.set('Select')
        price_entry.insert(0,row[5])
        quantity_entry.insert(0,row[6])
    else:
        pass

def recipt():
    app = customtkinter.CTk()
    app.geometry('500x450')
    app.title('customer Recipt')
    app.config(bg='plum')
    app.resizable(False,False)
    def View(id):
        conn = sqlite3.connect('Products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT item, quantity, price FROM Bill WHERE id= ?',(id,))
        rows = cursor.fetchall()
        for row in rows:
            tree.insert('',END,values=row)
        conn.close()
    
    def get_prices_and_quantity(id):
        conn = sqlite3.connect('Products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT price FROM Bill WHERE id= ?',(id,))
        price = [row[0] for row in cursor.fetchall()]
        cursor.execute('SELECT quantity FROM Bill WHERE id= ?',(id,))
        quantity = [row[0] for row in cursor.fetchall()]
        conn.close()
        return price,quantity
        
    style = ttk.Style(app)
    style.theme_use('clam')
    style.configure('Treeview',font=font3,foreground='purple',background='black',fieldbackground='purple')
    style.map('Treeview',background=[('selected','plum')])
    tree = ttk.Treeview(app)
    tree['columns'] = ('item','quantity','price')
    tree.column('#0',width=0,stretch=tk.NO)
    tree.column('item',anchor=tk.CENTER,width=100)
    tree.column('quantity',anchor=tk.CENTER,width=100)
    tree.column('price',anchor=tk.CENTER,width=100)
    tree.heading('item',text='item')
    tree.heading('quantity',text='quantity')
    tree.heading('price',text='price')
    tree.place(x=0,y=0)
    treeScroll = ttk.Scrollbar(app)
    treeScroll.configure(command=tree.yview)
    tree.configure(yscrollcommand=treeScroll.set)
    treeScroll.pack(side= RIGHT, fill= BOTH)
    tree.pack()
    
    total_label=customtkinter.CTkLabel(app,font=font2,text_color='black')
    total_label.place(x=250,y=250)
    
    selection = select_options.get()
    if selection != 'Select':
        View(selection)
    else:
        messagebox.showerror('Error','Select An Id to Show Bill.')
    if selection != 'Select':
        price,quantity = get_prices_and_quantity(selection)
        total = float(sum(price * quantity for price,quantity in zip(price,quantity)))
        total_label.configure(text = f'Total price:{total}')
    else:
        total = 0
        total_label.configure(text = f'Total price:{total}')
    app.mainloop()
    

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    item_options.set('')
    category_options.set('')
    price_entry.delete(0,END)
    quantity_entry.delete(0,END)

def show(*clicked):
    if clicked:
        item  = var1.get()
        show_price = database2.fetch_price(item)
        show_price_label= customtkinter.CTkLabel(frame,font=font2,text_color='black')
        show_price_label.place(x=30,y=380)
        show_price_label.configure(text = f'sale_price:{show_price}')
    
def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose a item to delete.')
    else:
        price = price_entry.get()
        id = id_entry.get()
        quantity = quantity_entry.get()
        item = var1.get()
        database2.delete_product(price,id,quantity)
        database2.udelete_stocks(item, quantity)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data has been deleted successfully.')
        
    
def add_to_treeview():
    products = database2.fetch_item()
    tree.delete(*tree.get_children())
    for product in products:
        tree.insert('', END, values=product)

def insert():
    id = id_entry.get()
    name = name_entry.get()
    today_date = f'{date.today():%y %m %d}'
    catogry = category_options.get()
    item = item_options.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    if not (id and name and item and quantity):
        messagebox.showerror('Error', 'Enter all fields.')
    else:
        try:
            price_value = int(price)
            database2.insert_product(id, name, today_date, catogry, item,price_value, quantity)
            add_to_treeview()
            clear()
            updated_stocks = database2.update_stocks(item, quantity)
        except ValueError:
            messagebox.showerror('Error', 'Quantity should be integer.')
        else:
            if updated_stocks == 0:
                messagebox.showerror('Error', 'Item out of stock. Choose another item.')
                
            else:
                messagebox.showinfo('Success', 'Data has been inserted.')
                messagebox.showinfo('Success', f'Stocks have been updated. New stock value: {updated_stocks}')


title_label = customtkinter.CTkLabel(app,font = font1,text='Customer Details',bg_color='purple',text_color='black')
title_label.place(x=30,y=15)

frame = customtkinter.CTkFrame(app,bg_color='black',fg_color='purple',corner_radius=10,border_width=2,border_color='black',width=210,height=600)
frame.place(x=25,y=45)

id_label= customtkinter.CTkLabel(frame,font=font2,text='Customer Id',text_color='black')
id_label.place(x=50,y=10)

id_entry= customtkinter.CTkEntry(frame,font=font2,text_color='black',fg_color='white',border_color='black',border_width=2,width=160)
id_entry.place(x=20,y=35)

name_label= customtkinter.CTkLabel(frame,font=font2,text='Customer Name',text_color='black')
name_label.place(x=50,y=70)

name_entry= customtkinter.CTkEntry(frame,font=font2,text_color='black',fg_color='white',border_color='black',border_width=2,width=160)
name_entry.place(x=20,y=105)

item_label= customtkinter.CTkLabel(frame,font=font2,text='Item',text_color='black')
item_label.place(x=50,y=140)

var1 = StringVar()
item_options = customtkinter.CTkComboBox(app,font=font2,variable = var1,text_color='black',fg_color='white',dropdown_hover_color='purple',button_color='white',button_hover_color='purple',border_color='purple',width=150,state='normal')
item_options.set('Select')
item_options.place(x=50,y=210)

category_label= customtkinter.CTkLabel(frame,font=font2,text='Category',text_color='black')
category_label.place(x=50,y=220)


category_options = customtkinter.CTkComboBox(app,font=font2,text_color='black',fg_color='white',dropdown_hover_color='purple',button_color='white',button_hover_color='purple',border_color='purple',width=150,state='normal')
category_options.set('Select')
category_options.place(x=50,y=290)

price_label= customtkinter.CTkLabel(frame,font=font2,text=' Price',text_color='black')
price_label.place(x=50,y=310)

price_entry= customtkinter.CTkEntry(frame,font=font2,text_color='black',fg_color='white',border_color='black',border_width=2,width=160)
price_entry.place(x=20,y=350)

quantity_label= customtkinter.CTkLabel(frame,font=font2,text=' Quantity',text_color='black')
quantity_label.place(x=50,y=410)

quantity_entry= customtkinter.CTkEntry(frame,font=font2,text_color='black',fg_color='white',border_color='black',border_width=2,width=160)
quantity_entry.place(x=20,y=450)

cart_button = customtkinter.CTkButton(frame,command=insert,font=font2,text_color='purple',text='Add to Cart',fg_color='black',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=8,width=80)
cart_button.place(x=40,y=480)

clear_button = customtkinter.CTkButton(frame,command = lambda:clear(True) ,font=font2,text_color='purple',text='Clear',fg_color='black',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=8,width=80)
clear_button.place(x=20,y=510)

delete_button = customtkinter.CTkButton(frame,command=delete,font=font2,text_color='purple',text='delete',fg_color='black',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=8,width=80)
delete_button.place(x=110,y=510)

title2_label = customtkinter.CTkLabel(app,font=font2,text='Bill Details',bg_color='purple',text_color='black')
title2_label.place(x=280,y=520)

frame2 = customtkinter.CTkFrame(app,bg_color='black',fg_color='purple',corner_radius=10,border_width=2,border_color='black',width=450,height=200)
frame2.place(x=280,y=540)

select_label = customtkinter.CTkLabel(frame2,font=font2,text='Select Customer Id to Get bill',bg_color='purple',text_color='black')
select_label.place(x=8,y=15)
var2 = StringVar()
select_options = customtkinter.CTkComboBox(frame2,variable=var2,font=font2,text_color='black',fg_color='white',dropdown_hover_color='purple',button_color='white',button_hover_color='purple',border_color='black',width=100,state='readonly')
select_options.set('Select')
select_options.place(x=40,y=40)

recipt_button = customtkinter.CTkButton(frame2,command=recipt,font=font2,text_color='purple',text='Recipt',fg_color='black',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=8,width=80)
recipt_button.place(x=200,y=40)


style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview',font=font3,foreground='purple',background='black',fieldbackground='purple')
style.map('Treeview',background=[('selected','plum')])

tree = ttk.Treeview(app,height=20)

tree['columns'] = ('ID','Customer_name','Date','Category','Item','Price','Quantity')

tree.column('#0',width=0,stretch=tk.NO)
tree.column('ID',anchor=tk.CENTER,width=100)
tree.column('Customer_name',anchor=tk.CENTER,width=100)
tree.column('Date',anchor=tk.CENTER,width=100)
tree.column('Category',anchor=tk.CENTER,width=100)
tree.column('Item',anchor=tk.CENTER,width=100)
tree.column('Price',anchor=tk.CENTER,width=100)
tree.column('Quantity',anchor=tk.CENTER,width=100)


tree.heading('ID',text='ID')
tree.heading('Customer_name',text='Customer_name')
tree.heading('Date',text='Date')
tree.heading('Category',text='Category')
tree.heading('Item',text='Item')
tree.heading('Price',text='Price')
tree.heading('Quantity',text='Quantity')


tree.place(x=260,y=50)
tree.bind('<ButtonRelease>',display_data)

treeScroll = ttk.Scrollbar(app)
treeScroll.configure(command=tree.yview)
tree.configure(yscrollcommand=treeScroll.set)
treeScroll.pack(side= RIGHT, fill= BOTH)
tree.pack()

var1.trace('w',show)
insert_item_options()
catogry_item_options()
add_to_treeview()
insert_ids_options()
app.mainloop()