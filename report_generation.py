import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from datetime import date

import sqlite3


app = customtkinter.CTk()
app.title('Report generation')
app.geometry('500x250')
app.resizable(False,False)
app.config(bg='plum')



font1 =('Arial',18,'bold')
font3 =('Arial',13,'bold')

def daily():
    app = customtkinter.CTk()
    app.geometry('500x300')
    app.title('Daily Report')
    app.config(bg='plum')
    app.resizable(True,True)
    today_date = f'{date.today():%y %m %d}'
    
    def fetch_details(date):
        conn = sqlite3.connect('Products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT item, quantity, price FROM Bill WHERE date= ?',(date,))
        rows = cursor.fetchall()
        for row in rows:
            tree.insert('',END,values=row)
        conn.close()
    
    def fetch(date):
        conn = sqlite3.connect('Products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT item, quantity, price FROM Bill WHERE date = ?',(date,))
        rows = cursor.fetchall()
        item = [p[0]for p in rows]
        quantity = [p[1]for p in rows]
        price = [j[2]for j in rows]
        conn.close()    
        return item,quantity,price
    items,quantity,price= fetch(today_date)
    
    def purchase_price(item):
        conn = sqlite3.connect('Products.db')
        cursor = conn.cursor()
        for i in item:
            cursor.execute('SELECT price FROM Products WHERE name = ?',(i,)) 
        rows = cursor.fetchall()
         
        return rows
    
    price2 = purchase_price(items)
     
   # purchase_price_items = float(sum(price2 * quantity for price2,quantity in zip(price2,quantity)))
    
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
    
    revenue_label=customtkinter.CTkLabel(app,font=font3,bg_color='purple',fg_color='purple',text_color='black')
    revenue_label.place(x=250,y=250)
    
    
    
    total = float(sum(price * quantity for price,quantity in zip(price,quantity)))
    revenue_label.configure(text = f'revenue:{total}')
    
    

    
    
    fetch_details(today_date)
    
    app.mainloop()


def monthly():
    app = customtkinter.CTk()
    app.geometry('500x500')
    app.title('monthly Report')
    app.config(bg='plum')
    app.resizable(True,True)
    
    def fetch_details(sdate,edate):
        conn = sqlite3.connect('Products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT item, quantity, price FROM Bill WHERE date BETWEEN ? AND ?',(sdate,edate))
        rows = cursor.fetchall()
        for row in rows:
            tree.insert('',END,values=row)
        conn.close()
    
    def fetch(sdate,edate):
        conn = sqlite3.connect('Products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Bill WHERE date BETWEEN ? AND ?',(sdate,edate))
        rows = cursor.fetchall()
        price = [j[5]for j in rows]
        quantity = [p[6]for p in rows]
        
        conn.close()    
        return quantity,price
    
    
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
    sdate = sdate_entry.get()
    edate = edate_entry.get()
    if not (sdate and edate ):
        messagebox.showerror('Error','Choose dates to Generate Report')
    revenue_label=customtkinter.CTkLabel(app,font=font3,bg_color='purple',fg_color='purple',text_color='black')
    revenue_label.place(x=250,y=250)
    quantity,price= fetch(sdate,edate)
    total = float(sum(price * quantity for price,quantity in zip(price,quantity)))
    revenue_label.configure(text = f'revenue:{total}')
    
    fetch_details(sdate,edate)
    
    app.mainloop()


def weekly():
    app = customtkinter.CTk()
    app.geometry('500x500')
    app.title('Weekly Report')
    app.config(bg='plum')
    app.resizable(True,True)
    
    def fetch_details(sdate,edate):
        conn = sqlite3.connect('Products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT item, quantity, price FROM Bill WHERE date BETWEEN ? AND ?',(sdate,edate))
        rows = cursor.fetchall()
        for row in rows:
            tree.insert('',END,values=row)
        conn.close()
    
    def fetch(sdate,edate):
        conn = sqlite3.connect('Products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Bill WHERE date BETWEEN ? AND ?',(sdate,edate))
        rows = cursor.fetchall()
        price = [j[5]for j in rows]
        quantity = [p[6]for p in rows]
        
        conn.close()    
        return quantity,price
    
    
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
    
    sdate = sdate_entry.get()
    edate = edate_entry.get()
    if not (sdate and edate ):
        messagebox.showerror('Error','Choose dates to Generate Report')
    revenue_label=customtkinter.CTkLabel(app,font=font3,bg_color='purple',fg_color='purple',text_color='black')
    revenue_label.place(x=250,y=250)
    quantity,price= fetch(sdate,edate)
    total = float(sum(price * quantity for price,quantity in zip(price,quantity)))
    revenue_label.configure(text = f'revenue:{total}')
    
    fetch_details(sdate,edate)
    
    app.mainloop()

sdate_label= customtkinter.CTkLabel(app,font=font1,text='Start date',text_color='black',fg_color='purple')
sdate_label.place(x=15,y=35)
sdate_entry= customtkinter.CTkEntry(app,font=font1,placeholder_text='23 08 05',text_color='black',fg_color='white',border_color='black',border_width=2,width=160)
sdate_entry.place(x=100,y=35)

edate_label= customtkinter.CTkLabel(app,font=font1,text='End date',text_color='black',fg_color='purple')
edate_label.place(x=15,y=80)
edate_entry= customtkinter.CTkEntry(app,font=font1,placeholder_text='23 08 05',text_color='black',fg_color='white',border_color='black',border_width=2,width=160)
edate_entry.place(x=100,y=80)

daily_button = customtkinter.CTkButton(app,command= daily,font=font1,text_color='black',text='Daily Report',fg_color='purple',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=10,width=100)
daily_button.place(x=15,y=150)
monthly_button = customtkinter.CTkButton(app,command=monthly,font=font1,text_color='black',text='Monthly Report',fg_color='purple',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=10,width=100)
monthly_button.place(x=150,y=150)
weekly_button = customtkinter.CTkButton(app,command=weekly,font=font1,text_color='black',text='week Report',fg_color='purple',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=10,width=100)
weekly_button.place(x=320,y=150)


app.mainloop()