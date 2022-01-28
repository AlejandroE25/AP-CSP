#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

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

loginButton = tk.Button(frameLogin, text="Log in", command=buttonTest).pack()

frameAuth = tk.Frame(root)
frameAuth.grid(row=0, column=0, sticky="news")


frameLogin.tkraise()

root.mainloop()
