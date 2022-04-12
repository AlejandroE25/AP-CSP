import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox

showGraph = False

top = Tk()


def helloCallBack():
    messagebox.showinfo("Hello Python", "Hello World")


B = Button(top, text="Hello", command=helloCallBack)

B.pack()
top.mainloop()

while not showGraph:
    pass

fig = plt.figure()
fig.subplots_adjust()
ax1 = fig.add_subplot(211)
ax1.set_ylabel('Retention (%)')
ax1.set_xlabel('Time (d)')
ax1.set_title('Retention Vs Time')

plt.ylim(0, 100)
plt.xlim(0, 31)

plt.xticks(np.arange(30))
plt.yticks(np.arange(0, 100, 10))

x = np.linspace(0, 30, 30)

y = np.exp(-x / 1)
line, = ax1.plot(x, y)

plt.show()
