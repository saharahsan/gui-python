import customtkinter
from tkinter import *
from tkinter import messagebox
import database

app = customtkinter.CTk()
app.title('Search Products')
app.geometry('700x600')
app.config(bg='plum')
app.resizable(False,False)

font1 = ('Arial',30,'bold')
font2 = ('Arial',20,'bold')

def search_product():
    selection = variable3.get()
    selection2 = variable.get()
    if (selection != 'Select'):
        row = database.search_product_id(selection)
        name_result_label.configure(text=row[1])
        catogry_result_label.configure(text=row[2])
        stock_result_label.configure(text=row[3])
        price_result_label.configure(text=row[5])
    elif ( selection2 != 'Select'):
        row = database.search_product_name(selection2)
        name_result_label.configure(text=row[1])
        catogry_result_label.configure(text=row[2])
        stock_result_label.configure(text=row[3])
        price_result_label.configure(text=row[5])
        
         
    else:
        messagebox.showerror('Error','Select Id')
        

def insert_item_options():
    item = database.fetch_all_item()
    item_options.configure(values=item)

def insert_ids_options():
    ids = database.fetch_all_ids()
    ids_options.configure(values=ids)
    

title_label = customtkinter.CTkLabel(app,font = font1,text='Search Products',bg_color='purple',text_color='black')
title_label.place(x=250,y=15)

name_label = customtkinter.CTkLabel(app,font = font2,text='Search by name:',bg_color='purple',text_color='black')
name_label.place(x=50,y=100)
variable = StringVar()

item_options = customtkinter.CTkComboBox(app,font=font2,text_color='black',fg_color='white',dropdown_hover_color='purple',button_color='white',button_hover_color='purple',border_color='purple',width=150,variable=variable,state='readonly')
item_options.set('Select')
item_options.place(x=200,y=100)

search_label = customtkinter.CTkLabel(app,font = font2,text='Search by Id:',bg_color='purple',text_color='black')
search_label.place(x=50,y=130)
variable3 = StringVar()

ids_options = customtkinter.CTkComboBox(app,font=font2,text_color='black',fg_color='white',dropdown_hover_color='purple',button_color='white',button_hover_color='purple',border_color='purple',width=150,variable=variable3,state='readonly')
ids_options.set('Select')
ids_options.place(x=200,y=130)

search_button = customtkinter.CTkButton(app,command=search_product,font=font2,text='Search',text_color='black',fg_color='purple',hover_color='plum',bg_color='black',border_color='black',cursor='hand2',corner_radius=7,width=100)
search_button.place(x=360,y=100)

frame = customtkinter.CTkFrame(app,bg_color='#dda0dd',fg_color='black',corner_radius=10,border_width=5,border_color='purple',width=500,height=300)
frame.place(x=60,y=180)

name_label = customtkinter.CTkLabel(frame,font = font2,text='Name:',bg_color='purple',text_color='black')
name_label.place(x=20,y=50)

catogry_label = customtkinter.CTkLabel(frame,font = font2,text='Catogry:',bg_color='purple',text_color='black')
catogry_label.place(x=230,y=50)

stock_label = customtkinter.CTkLabel(frame,font = font2,text='stocks:',bg_color='purple',text_color='black')
stock_label.place(x=20,y=200)

price_label = customtkinter.CTkLabel(frame,font = font2,text='Price:',bg_color='purple',text_color='black')
price_label.place(x=230,y=200)

name_result_label = customtkinter.CTkLabel(frame,font = font2,text='',bg_color='purple',text_color='black')
name_result_label.place(x=100,y=50)

catogry_result_label = customtkinter.CTkLabel(frame,font = font2,text='',bg_color='purple',text_color='black')
catogry_result_label.place(x=330,y=50)

stock_result_label = customtkinter.CTkLabel(frame,font = font2,text='',bg_color='purple',text_color='black')
stock_result_label.place(x=100,y=200)

price_result_label = customtkinter.CTkLabel(frame,font = font2,text='',bg_color='purple',text_color='black')
price_result_label.place(x=310,y=200)

insert_ids_options()
insert_item_options()
app.mainloop()