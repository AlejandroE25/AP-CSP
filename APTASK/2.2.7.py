import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox
import math
import time



def findNumTrial1(timeIn=0.0, s_In=0.0):
    if timeIn == 0:
        t = (float(input("How many days has it been since you've studied \n")))
    else:
        t = timeIn

    if s_In == 0:
        S = (float(input("How stable would you say your memory is (From 0% to 100%, don't use the % symbol)\n")))
    else:
        S = s_In
    exponentNumber = -t / S

    R = math.e ** exponentNumber
    return R, t, S


retrievability, ogTime, stability = findNumTrial1()
print(f"Retrievability = {round(retrievability * 100, 2)}%, Time = {ogTime} days")

userReq = float(input("\nHow retrievable must this knowledge be by the time you need it? (Enter as percent, don't use the % symbol)\n"))/100  #Just to make more user friendly

if retrievability < userReq:
    timeOut = ogTime
    while not retrievability >= userReq:
        retrievability, timeOut, uselessVariable = findNumTrial1(timeIn=timeOut - (1/24), s_In=stability) #Reduce the count by an hour each time.  I think it works.  It seems to work just fine after all.
else:
    print("You're all good! \n Good luck!")
    exit()


print(f"To reach a retrievability of {userReq * 100}%, you must study no longer than {round(timeOut * 24)} hours, or {round(timeOut)} days before your test")


'''
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
'''