import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from subprocess import call

app = customtkinter.CTk()
app.title('Utility Store Management System(user)')
app.geometry('450x380')
app.resizable(False,False)
app.config(bg='plum')
def inventory():
    call(["python","inventory_user.py"])
def search():
    call(["python","search.py"])   

def logout():
    sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if sure == True:
        app.destroy()
def bill():
    call(["python","bill.py"])
def report():
    call(["python","report_generation.py"])

font1 =('Arial',18,'bold')
inventory_button = customtkinter.CTkButton(app,command=inventory,font=font1,text_color='black',text='Inventory',fg_color='purple',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=10,width=100)
inventory_button.place(x=15,y=150)
search_button = customtkinter.CTkButton(app,command=search,font=font1,text_color='black',text='Search',fg_color='purple',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=10,width=100)
search_button.place(x=130,y=150)
report_button = customtkinter.CTkButton(app,command=report,font=font1,text_color='black',text='Report generation',fg_color='purple',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=10,width=100)
report_button.place(x=240,y=150)
bill_button = customtkinter.CTkButton(app,command = bill,font=font1,text_color='black',text='Create Bill',fg_color='purple',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=10,width=100)
bill_button.place(x=70,y=200)
logout_button = customtkinter.CTkButton(app,command=logout,font=font1,text_color='black',text='logout',fg_color='purple',hover_color='plum',bg_color='black',cursor='hand2',corner_radius=10,width=100)
logout_button.place(x=200,y=200)





    

app.mainloop()