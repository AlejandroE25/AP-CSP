#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
from tkinter import scrolledtext
from tkinter.scrolledtext import *

enteredPass = None


def buttonTest():
    global enteredPass
    enteredPass = passVar.get()

    passAuthLabel = tk.Label(frameAuth, font="Consolas", text=enteredPass).pack()
    frameAuth.tkraise()

    print(enteredPass, " - Button Test")


# main window
root = tk.Tk()
root.wm_geometry("140x200")
root.title('Authorization')

passVar = tk.StringVar()
userVar = tk.StringVar()

frameLogin = tk.Frame(root)
frameLogin.grid(row=0, column=0, sticky="news")

usernameLabel = tk.Label(frameLogin, text='Username:', font="Consolas").pack()
userEnt = tk.Entry(frameLogin, bd=3, textvariable=userVar).pack(pady=5, padx=5)

passwordLabel = tk.Label(frameLogin, text="Password:", font="Consolas").pack()
passEnt = tk.Entry(frameLogin, bd=3, textvariable=passVar, show="·").pack(pady=5, padx=5)

# Add this code before the code that creates your "Login" button
bt_image = tk.PhotoImage(file="button.gif")
bt_image = bt_image.subsample(10, 10)

loginButton = tk.Button(frameLogin, text="Log in", command=buttonTest, image=bt_image).pack()

frameAuth = tk.Frame(root)
frameAuth.grid(row=0, column=0, sticky="news")

frameLogin.tkraise()

testTextbox = ScrolledText(frameAuth)
testTextbox.configure(height=10, width=50)
testTextbox.pack()

root.mainloop()
