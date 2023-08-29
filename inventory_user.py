import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from datetime import date
from tkinter import messagebox
import database

app = customtkinter.CTk()
app.title('inventory management (user)')
app.geometry('1200x680')
app.config(bg='plum')
app.resizable(False,False)

font1 =('Arial',25,'bold')
font2 =('Arial',18,'bold')
font3 =('Arial',13,'bold')

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    catogry_entry.delete(0,END)
    stock_entry.delete(0,END)
    price_entry.delete(0,END)
    sale_price_entry.delete(0,END)

def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose a product to delete.')
    else:
        id = id_entry.get()
        database.delete_product(id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data has been deleted successfully.')

def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose a product to update.')
    else:
        id = id_entry.get()
        name = name_entry.get()
        catogry = catogry_entry.get()
        stock = stock_entry.get()
        price= price_entry.get()
        sale_price = sale_price_entry.get()
        today_date = f'{date.today():%y %m %d}'
        database.update_product(name,catogry,stock, price,sale_price,today_date, id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data have been updated successfully.')


def add_to_treeview():
    products = database.fetch_products()
    tree.delete(*tree.get_children())
    for product in products:
        tree.insert('', END, values=product)

def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        id_entry.insert(0,row[0])
        name_entry.insert(0,row[1])
        catogry_entry.insert(0,row[2])
        stock_entry.insert(0,row[3])
        price_entry.insert(0,row[4])
        sale_price_entry.insert(0,row[5])
    else:
        pass

title_label = customtkinter.CTkLabel(app,font = font1,text='Product details',bg_color='purple',text_color='black')
title_label.place(x=30,y=15)

frame = customtkinter.CTkFrame(app,bg_color='black',fg_color='purple',corner_radius=10,border_width=2,border_color='black',width=200,height=600)
frame.place(x=25,y=45)

image1 = PhotoImage(file="1.png")
image1_label = Label(frame,image=image1,bg='black')
image1_label.place(x=65,y=5)

id_label= customtkinter.CTkLabel(frame,font=font2,text='Product Id',text_color='black')
id_label.place(x=50,y=75)

id_entry= customtkinter.CTkEntry(frame,font=font2,text_color='black',fg_color='white',border_color='black',border_width=2,width=160)
id_entry.place(x=20,y=105)

name_label= customtkinter.CTkLabel(frame,font=font2,text='Product Name',text_color='black')
name_label.place(x=50,y=140)

name_entry= customtkinter.CTkEntry(frame,font=font2,text_color='black',fg_color='white',border_color='black',border_width=2,width=160)
name_entry.place(x=20,y=175)

catogry_label= customtkinter.CTkLabel(frame,font=font2,text='Product Catogry',text_color='black')
catogry_label.place(x=50,y=205)

catogry_entry= customtkinter.CTkEntry(frame,font=font2,text_color='black',fg_color='white',border_color='black',border_width=2,width=160)
catogry_entry.place(x=20,y=240)

stock_label= customtkinter.CTkLabel(frame,font=font2,text='Product Stock',text_color='black')
stock_label.place(x=50,y=275)

stock_entry= customtkinter.CTkEntry(frame,font=font2,text_color='black',fg_color='white',border_color='black',border_width=2,width=160)
stock_entry.place(x=20,y=305)

price_label= customtkinter.CTkLabel(frame,font=font2,text='Product Price',text_color='black')
price_label.place(x=50,y=340)

price_entry= customtkinter.CTkEntry(frame,font=font2,text_color='black',fg_color='white',border_color='black',border_width=2,width=160)
price_entry.place(x=20,y=380)

sale_price_label= customtkinter.CTkLabel(frame,font=font2,text='Sale Price',text_color='black')
sale_price_label.place(x=50,y=410)

sale_price_entry= customtkinter.CTkEntry(frame,font=font2,text_color='black',fg_color='white',border_color='black',border_width=2,width=160)
sale_price_entry.place(x=20,y=450)

clear_button = customtkinter.CTkButton(frame,command=lambda:clear(True) ,font=font2,text_color='purple',text='Clear',fg_color='black',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=8,width=80)
clear_button.place(x=60,y=500)

update_button = customtkinter.CTkButton(frame,command=update,font=font2,text_color='purple',text='Update',fg_color='black',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=8,width=80)
update_button.place(x=15,y=530)

delete_button = customtkinter.CTkButton(frame,command=delete,font=font2,text_color='purple',text='Delete',fg_color='black',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=8,width=80)
delete_button.place(x=108,y=530)

style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview',font=font3,foreground='purple',background='black',fieldbackground='purple')
style.map('Treeview',background=[('selected','plum')])

tree = ttk.Treeview(app,height=30)

tree['columns'] = ('ID','Name','Catogry','In_stock','Price','Sale_price','Date')

tree.column('#0',width=0,stretch=tk.NO)
tree.column('ID',anchor=tk.CENTER,width=100)
tree.column('Name',anchor=tk.CENTER,width=100)
tree.column('Catogry',anchor=tk.CENTER,width=100)
tree.column('In_stock',anchor=tk.CENTER,width=100)
tree.column('Price',anchor=tk.CENTER,width=100)
tree.column('Sale_price',anchor=tk.CENTER,width=100)
tree.column('Date',anchor=tk.CENTER,width=100)

tree.heading('ID',text='ID')
tree.heading('Name',text='Name')
tree.heading('Catogry',text='Catogry')
tree.heading('In_stock',text='In_stock')
tree.heading('Price',text='Price')
tree.heading('Sale_price',text='Sale_price')
tree.heading('Date',text='Date')

tree.place(x=300,y=50)
tree.bind('<ButtonRelease>',display_data)
treeScroll = ttk.Scrollbar(app)
treeScroll.configure(command=tree.yview)
tree.configure(yscrollcommand=treeScroll.set)
treeScroll.pack(side= RIGHT, fill= BOTH)
tree.pack()

add_to_treeview()
app.mainloop()