import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox
import math
import time
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter.filedialog import asksaveasfilename
import subprocess

# Make the math a function to put the button to and then make the user input the answers in the label bar so and then hit the button to process the numbers and input them into the equation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
frame = Frame(root)
frame.configure(height=600, width=400, bg="#2e2e2e")
frame.pack()

fig = plt.figure(figsize=(2, 2))
fig.subplots_adjust()


retentionChart = FigureCanvasTkAgg(fig, frame)
retentionChart.get_tk_widget().pack()

daysSinceLabel = Label(frame, text="How many days since you last studied?", bg="#2e2e2e", fg="white").pack(pady=(30, 10))
daysSinceInput = Text(frame, bg="black", fg="white", width=10, height=1).pack()

stabilitySliderLabel = Label(frame, text="How stable is your memory as a %", bg="#2e2e2e", fg="white").pack(pady=(30,10))
mentalStabilitySlider = Scale(frame, from_=0, to=100, length=200, orient=HORIZONTAL, bg="#2e2e2e", fg="white", bd=0).pack()


def findNumTrial1(timeIn=0.0, s_In=0.0):
    global daysSinceInput
    global mentalStabilitySlider

    if timeIn == 0:
        t = int(daysSinceInput.get())
    else:
        t = timeIn

    if s_In == 0:
        stability = (float(input(
            f"How stable would you say your memory is? {colouredText('(From 0% to 100%, do not use the % symbol)', colors.blue)}\n")))
    else:
        stability = s_In
    exponentNumber = -t / stability

    R = math.e ** exponentNumber
    print(R, t, stability)
    return R, t, stability


def plotGraph(days, stability):
    global fig
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('Retention (%)')
    ax1.set_xlabel('Time (d)')
    ax1.set_title('Retention Vs Time')

    plt.ylim(0, 100)
    plt.xlim(0, 31)

    plt.xticks(np.arange(days))
    plt.yticks(np.arange(0, 100, 10))

    x = np.linspace(0, days)

    y = (math.e ** -(x / stability)) * 100
    line, = ax1.plot(x, y)
    plt.autoscale(True, "x", True)



plotGraphButton = Button(frame, text="Plot Graph", command=findNumTrial1).pack()

OutputTextbox = tksc.ScrolledText(frame, height=5, width=100, bg="#2e2e2e", fg="white")
OutputTextbox.pack(pady=(20,0))
OutputTextbox.insert(tk.END, 'Please enter the information requested')
OutputTextbox.config(state='disabled')



root.mainloop()



pref = "\033["
reset = f"{pref}0m"


def colouredText(text, colour):
    global reset
    return f"{colour}{text}{reset}"


class colors:
    black = pref + "30m"
    red = pref + "31m"
    green = pref + "32m"
    yellow = pref + "33m"
    blue = pref + "34m"
    magenta = pref + "35m"
    cyan = pref + "36m"
    white = pref + "37m"


varDict = {
    # Creates a dictionary.  It's like a list, but instead of using a number as an index, you can use a name.
    "Retrieveability": None,
    "Original Time": None,
    "Memory Stability": None,
    "User Requirement": None
}

varDict["Retrieveability"], varDict["Original Time"], varDict["Memory Stability"] = findNumTrial1()
print(
    f"\nRetrievability = {colouredText(str(round(varDict['Retrieveability'] * 100, 2)), colors.green)}%, Time = {colouredText(str(varDict['Original Time']), colors.green)} days")

varDict["User Requirement"] = float(input(
    f"\nHow retrievable must this knowledge be by the time you need it? {colouredText('(Enter as percent, do not use the % symbol)', colors.blue)}\n")) / 100  # Just to make more user friendly

timeOut = varDict["Original Time"]

if varDict["Retrieveability"] < varDict["User Requirement"]:
    while not varDict["Retrieveability"] >= varDict["User Requirement"]:
        varDict["Retrieveability"], timeOut, varDict["Memory Stability"] = findNumTrial1(
            timeIn=timeOut - (1 / 24), s_In=varDict[
                "Memory Stability"])  # Reduce the count by an hour each time.  I think it works.  It seems to work just fine after all.
    # End of while loop
    print(
        f"To reach a retrievability of {colouredText(str(varDict['User Requirement'] * 100), colors.yellow)}%, you must study no longer than {colouredText(round(timeOut * 24, 2), colors.green)} hours, or {colouredText(round(timeOut, 1), colors.green)} days before your test")
else:
    print("You're all good! \nGood luck!")
