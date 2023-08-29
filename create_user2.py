import customtkinter
import sqlite3
import bcrypt
from subprocess import call
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

app = customtkinter.CTk()
app.title('sign_up / login')
app.geometry('800x560')
app.config(bg='black')

font1 = ('Arial',25,'bold','italic')
font2 = ('Arial',18,'bold')
font3 = ('Arial',13,'bold')
font4 = ('Arial',13,'bold','underline')

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
      CREATE TABLE IF NOT EXISTS Admin(
         username TEXT NOT NULL,
         password TEXT NOT NULL 
      ) ''')
cursor.execute('''
      CREATE TABLE IF NOT EXISTS User(
         username TEXT NOT NULL,
         password TEXT NOT NULL 
      ) ''')

def signup():
      type = type_entry.get()
      username = username_entry.get()
      password = password_entry.get()
      if username!='' and password !='' and type =='user':
            cursor.execute('SELECT username FROM User WHERE username=?',[username])
            if cursor.fetchone() is not None:
                  messagebox.showerror('Error','User name already Exists.')
            else:
                  encoded_password = password.encode('utf-8')
                  hashed_password = bcrypt.hashpw(encoded_password,bcrypt.gensalt())
                  print(hashed_password)
                  cursor.execute('INSERT INTO User VALUES (?, ?)',[username,hashed_password])
                  conn.commit()
                  messagebox.showinfo('success','User Account has been created successfully.')
     
      else:
            messagebox.showerror('Error','Enter all data.')
 
          
frame1 = customtkinter.CTkFrame(app,bg_color='black',fg_color='black',width=800,height=560)
frame1.place(x=0,y=0)

image1 = PhotoImage(file="2.png")
image1_label= Label(frame1,image=image1,bg='black')
image1_label.place(x=0,y=0)

signup_label = customtkinter.CTkLabel(frame1,font=font1,text='sign_up',bg_color='purple',text_color='black')
signup_label.place(x=560,y=20)

type_label = customtkinter.CTkLabel(frame1,font=font2,text='Select Type of Account:',bg_color='purple',text_color='black')
type_label.place(x=560,y=80)

type_entry = customtkinter.CTkEntry(frame1,font=font2,text_color='black',fg_color='white',bg_color='black',border_color='black',border_width=3,placeholder_text='user',placeholder_text_color='black',width=200,height=50)
type_entry.place(x=560,y=120)

username_entry = customtkinter.CTkEntry(frame1,font=font2,text_color='black',fg_color='white',bg_color='black',border_color='black',border_width=3,placeholder_text='Username',placeholder_text_color='black',width=200,height=50)
username_entry.place(x=560,y=190)

password_entry = customtkinter.CTkEntry(frame1,font=font2,show='*',text_color='black',fg_color='white',bg_color='black',border_color='black',border_width=3,placeholder_text='password',placeholder_text_color='black',width=200,height=50)
password_entry.place(x=560,y=260)

signup_button = customtkinter.CTkButton(frame1,command=signup,font=font3,text_color='black',text='Sign up',fg_color='purple',hover_color='plum',bg_color='black',corner_radius=5,cursor='hand2',width=120)
signup_button.place(x=560,y=320)



app.mainloop()

