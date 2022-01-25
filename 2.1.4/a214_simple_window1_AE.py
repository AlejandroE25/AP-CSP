#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x100")
root.title('Authorization')

frameLogin = tk.Frame(root)
frameLogin.grid()

usernameLabel = tk.Label(frameLogin, text='Username:').pack()

passwordLabel = tk.Label(frameLogin, text="Password:", font="Courier").pack()

root.mainloop()
