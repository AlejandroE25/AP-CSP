from logging import root
import tkinter as tk
from turtle import bgcolor, color

root = tk.Tk()

root.configure(background='blue')
root.columnconfigure(1, weight=1)

redFrame = tk.Frame(master=root)
redFrame.configure(bg='red')
redFrame.grid(row=1, column=0)

blankLabel = tk.Label(redFrame, text="                                                          \n                                                            \n                                                                 ", bg="red").pack()

root.geometry('400x400')
root.title("COLOUR GRID")
root.mainloop()