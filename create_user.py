import customtkinter
import sqlite3
import bcrypt
from subprocess import call
from tkinter import *
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
      if username!='' and password !='' and type =='admin':
            cursor.execute('SELECT username FROM Admin WHERE username=?',[username])
            if cursor.fetchone() is not None:
                  messagebox.showerror('Error','User name already Exists.')
            else:
                  encoded_password = password.encode('utf-8')
                  hashed_password = bcrypt.hashpw(encoded_password,bcrypt.gensalt())
                  print(hashed_password)
                  cursor.execute('INSERT INTO Admin VALUES (?, ?)',[username,hashed_password])
                  conn.commit()
                  messagebox.showinfo('success','Admin Account has been created successfully.')
      elif type=='user' and username!='' and password !='':
            cursor.execute('SELECT username FROM User WHERE username= ?',[username])
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
 
          
          
def login():
      frame1.destroy()
      frame2 = customtkinter.CTkFrame(app,bg_color='black',fg_color='black',width=800,height=560)
      frame2.place(x=0,y=0) 
      
      image1  = PhotoImage(file="2.png")
      image1_label= Label(frame2,image=image1,bg='black')
      image1_label.place(x=0,y=0)
      frame2.image1 = image1
      
      login_label = customtkinter.CTkLabel(frame2,font=font1,text='Login',bg_color='purple',text_color='black')
      login_label.place(x=560,y=20)
      
      global username_entry2
      global password_entry2
      global type_entry2

      type_entry2 = customtkinter.CTkEntry(frame2,font=font2,text_color='black',fg_color='white',bg_color='black',border_color='black',border_width=3,placeholder_text='admin or user',placeholder_text_color='black',width=200,height=50)
      type_entry2.place(x=560,y=80) 
      
      username_entry2 = customtkinter.CTkEntry(frame2,font=font2,text_color='black',fg_color='white',bg_color='black',border_color='black',border_width=3,placeholder_text='Username',placeholder_text_color='black',width=200,height=50)
      username_entry2.place(x=560,y=140)
      
      password_entry2 = customtkinter.CTkEntry(frame2,show='*',font=font2,text_color='black',fg_color='white',bg_color='black',border_color='black',border_width=3,placeholder_text='Password',placeholder_text_color='black',width=200,height=50)
      password_entry2.place(x=560,y=200)
      
      login_button2 = customtkinter.CTkButton(frame2,command=login_account,font=font4,text_color='black',text='Login',fg_color='purple',hover_color='plum',bg_color='black',corner_radius=5,cursor='hand2',width=40)
      login_button2.place(x=560,y=260)
      
      
def login_account():
      type = type_entry2.get()
      username =  username_entry2.get()
      password = password_entry2.get()
      if username!='' and password !='' and type =='admin':
            cursor.execute('SELECT password FROM Admin WHERE username=?',[username])
            result = cursor.fetchone()
            if result:
                  if bcrypt.checkpw(password.encode('utf-8'),result[0]):
                        messagebox.showinfo('Success','Admin logged in successfully.')
                        call(["python","navigation.py"])
                  else:
                        messagebox.showerror('Error','Invalid password!')
            else:
                  messagebox.showerror('Error','Invalid username')
      elif username!='' and password !='' and type =='user':
            cursor.execute('SELECT password FROM User WHERE username=?',[username])
            result = cursor.fetchone()
            if result:
                  if bcrypt.checkpw(password.encode('utf-8'),result[0]):
                        messagebox.showinfo('Success','User logged in successfully.')
                        call(["python","navigation2.py"])
                  else:
                        messagebox.showerror('Error','Invalid password!')
            else:
                  messagebox.showerror('Error','Invalid username')
      else:
            messagebox.showerror('Error','Enter all fields.')
            
        
          

frame1 = customtkinter.CTkFrame(app,bg_color='black',fg_color='black',width=800,height=560)
frame1.place(x=0,y=0)

image1 = PhotoImage(file="2.png")
image1_label= Label(frame1,image=image1,bg='black')
image1_label.place(x=0,y=0)

signup_label = customtkinter.CTkLabel(frame1,font=font1,text='sign_up',bg_color='purple',text_color='black')
signup_label.place(x=560,y=20)

type_label = customtkinter.CTkLabel(frame1,font=font2,text='Select Type of Account:',bg_color='purple',text_color='black')
type_label.place(x=560,y=80)

type_entry = customtkinter.CTkEntry(frame1,font=font2,text_color='black',fg_color='white',bg_color='black',border_color='black',border_width=3,placeholder_text='admin or user',placeholder_text_color='black',width=200,height=50)
type_entry.place(x=560,y=120)

username_entry = customtkinter.CTkEntry(frame1,font=font2,text_color='black',fg_color='white',bg_color='black',border_color='black',border_width=3,placeholder_text='Username',placeholder_text_color='black',width=200,height=50)
username_entry.place(x=560,y=190)

password_entry = customtkinter.CTkEntry(frame1,font=font2,show='*',text_color='black',fg_color='white',bg_color='black',border_color='black',border_width=3,placeholder_text='password',placeholder_text_color='black',width=200,height=50)
password_entry.place(x=560,y=260)

signup_button = customtkinter.CTkButton(frame1,command=signup,font=font3,text_color='black',text='Sign up',fg_color='purple',hover_color='plum',bg_color='black',corner_radius=5,cursor='hand2',width=120)
signup_button.place(x=560,y=320)

login_label = customtkinter.CTkEntry(frame1,font=font2,text_color='black',fg_color='purple',bg_color='black',border_color='black',border_width=3,placeholder_text='Do have an account?',placeholder_text_color='black',width=200,height=50)
login_label.place(x=560,y=360)

login_button = customtkinter.CTkButton(frame1,command=login,font=font4,text_color='black',text='Login',fg_color='purple',hover_color='plum',bg_color='black',corner_radius=5,cursor='hand2',width=40)
login_button.place(x=560,y=410)

app.mainloop()