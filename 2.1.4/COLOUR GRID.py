import tkinter as tk

root = tk.Tk()
root.wm_geometry("400x400")
root.title("I\'m Gonna Cry")


Canvas = tk.Canvas(root, width=400, height=400)
Canvas.pack()

blueRec = Canvas.create_rectangle(0, 0, 400, 400, fill='blue')
redRec = Canvas.create_rectangle(0, 200, 250, 400, fill="red")
greenRec = Canvas.create_rectangle(250, 0, 400, 200, fill='lime')
yellowRec = Canvas.create_rectangle(250, 200, 400, 400, fill="yellow")


root.mainloop()
