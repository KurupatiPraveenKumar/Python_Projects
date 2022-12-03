import tkinter
from tkinter import *
from tkinter import messagebox


def Ok():
    username=e1.get()
    password=e2.get()

    if(username == "" and password == ""):
        messagebox.showinfo("","Blocks are empty Please enter")

    elif(username == "Admin" and password == "123"):
        messagebox.showinfo("","Login Sucess")
        root.destroy()

    else:
        messagebox.showinfo("","incorrect password")

root = Tk()
root.title("Login")
root.geometry("400x400")
global e1
global e2

Label(root,text="UserName").place(x=10,y=10)
Label(root,text="Password").place(x=10,y=40)

e1 = Entry(root)
e1.place(x=140,y=10)

e2 = Entry(root)
e2.place(x=140,y=40)
e2.config(show="*")

Button(root,text="Login",command=Ok,height=3,width=13).place(x=10,y=100)

root.mainloop()
