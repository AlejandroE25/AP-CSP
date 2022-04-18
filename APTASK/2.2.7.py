import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox
import math
import time

pref = "\033["
reset = f"{pref}0m"


class colors:
    black = pref + "30m"
    red = pref + "31m"
    green = pref + "32m"
    yellow = pref + "33m"
    blue = pref + "34m"
    magenta = pref + "35m"
    cyan = pref + "36m"
    white = pref + "37m"


def findNumTrial1(timeIn=0.0, s_In=0.0):
    if timeIn == 0:
        t = (float(input("How many days has it been since you've studied \n")))
    else:
        t = timeIn

    if s_In == 0:
        S = (float(input(
            f"How stable would you say your memory is? {colors.blue}(From 0% to 100%, don't use the % symbol){reset}\n")))
    else:
        S = s_In
    exponentNumber = -t / S

    R = math.e ** exponentNumber
    return R, t, S


varDict = {
    # Creates a dictionary.  It's like a list, but instead of using a number as an index, you can use a name.
    "Retrieveability": 0,
    "Original Time": 0,
    "Memory Stability": 0,
    "User Requirement": 0
}

varDict["Retrieveability"], varDict["Original Time"], varDict["Memory Stability"] = findNumTrial1()
print(f"\nRetrievability = {colors.green}" + str(
    round(varDict["Retrieveability"] * 100, 2)) + f"{reset}%, Time = {colors.green}" + str(
    varDict["Original Time"]) + f"{reset} days")

varDict["User Requirement"] = float(input(
    f"\nHow retrievable must this knowledge be by the time you need it? {colors.blue}(Enter as percent, don't use the % symbol){reset}\n")) / 100  # Just to make more user friendly

timeOut = varDict["Original Time"]

if varDict["Retrieveability"] < varDict["User Requirement"]:
    while not varDict["Retrieveability"] >= varDict["User Requirement"]:
        varDict["Retrieveability"], timeOut, varDict["Memory Stability"] = findNumTrial1(
            timeIn=timeOut - (1 / 24), s_In=varDict[
                "Memory Stability"])  # Reduce the count by an hour each time.  I think it works.  It seems to work just fine after all.
    # End of while loop
    print(f"To reach a retrievability of {colors.yellow}" + str(varDict[
                                                                    "User Requirement"] * 100) + f"{reset}%, you must study no longer than {colors.green}{round(timeOut * 24, 2)}{reset} hours, or {colors.green}{round(timeOut, 1)}{reset} days before your test")
else:
    print("You're all good! \nGood luck!")

'''
fig = plt.figure()
fig.subplots_adjust()
ax1 = fig.add_subplot(211)
ax1.set_ylabel('Retention (%)')
ax1.set_xlabel('Time (d)')
ax1.set_title('Retention Vs Time')

plt.ylim(0, 100)
plt.xlim(0, 31)

plt.xticks(np.arange(timeOut))
plt.yticks(np.arange(0, 100, 10))

x = np.linspace(0, timeOut)

y = (math.e ** -(x / varDict["Memory Stability"])) * 100
line, = ax1.plot(x, y)
plt.autoscale(True, "x", True)
plt.show()
'''