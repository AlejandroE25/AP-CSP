import math
import string
import time
import random
import os

# The different tests & test list
Animal = ["Cat", "Dog", "Bird", "Mouse", "Bunny", "Cow", "Horse", "Giraffe", "Elephant", "Sheep"]
Number = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
Vehicle = ["Car", "Truck", "Train", "Van", "Boat", "Plane", "Submarine", "Bike", "Motorcycle", "Rocket"]
Object = ["Fork", "House", "Balloon", "Shovel", "Camera", "Table", "Mirror", "Shoe", "Paper", ""]
Color = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Indigo", "Gray", "Brown", "Pink"]

testList = {
   "Animal": Animal,
   "Number": Number,
   "Vehicle": Vehicle,
   "Object": Object,
   "Color": Color
}

testSample = []

# Asks if user has taken test and then initiates the test
while True:
   userInput = input("Have you taken the memory test? (Y/N) ")
   if userInput.upper() == "Y":
       break
   elif userInput.upper() == "N":
       testToTake = testList[string.capwords(input("What test do you want to take? (Animal, Number, Vehicle, Object, or Color) "))]
       for indxs in testToTake:
           testSample.append(indxs)
       random.shuffle(testToTake)
       testAnswer = testToTake
       print(testToTake)
       time.sleep(5)
       os.system('cls || clear')

       listInput = 0
       testInput = []
       # Asks the user for answers for the test
       while listInput != 10:
           print("Word Bank:", testSample)
           testInputIndex = string.capwords(input("Write the words in order as you saw them one at a time. "))
           if testInputIndex in testAnswer:
               testInput.append(testInputIndex)
               print("\n", "Answer:", testInput, "\n")
               listInput += 1
           elif testInputIndex in testInput:
               print(f"'{testInputIndex}' is already in the list")
           else:
               print(f"'{testInputIndex}' is not a valid answer")
           time.sleep(3)
           os.system('cls || clear')
       # Checks for correct answers
       print(f"The correct answers are {testAnswer}")
       correct = 0
       while len(testInput) > 0:
           if testAnswer[0] == testInput[0]:
               correct += 1
           del testAnswer[0]
           del testInput[0]
       # Calculates and displays test answer
       testScore = correct * 10
       print("\n", f"Your test score & memory strength is {testScore}%")

       break

   else:
       print("Please give a valid response")

# Where the working code starts

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


def findNumTrial1(timeIn=None, s_In=None):
   if timeIn is None:
       t = (float(input("How many days has it been since you've studied \n")))
   else:
       t = timeIn

   if s_In is None:
       stability = (float(input(
           f"How is strong is your memory based on your test result? {colouredText('(From 0% to 100%, do not use the % symbol)', colors.blue)}\n")))

   else:
       stability = s_In
   exponentNumber = -t / stability

   R = math.e ** exponentNumber
   return R, t, stability


varDict = {
   # Creates a dictionary.  It's like a list, but instead of using a number as an index, you can use a name.
   "Retrieveability": None,
   "Original Time": None,
   "Memory Stability": None,
   "User Requirement": None
}

varDict["Retrieveability"], varDict["Original Time"], varDict["Memory Stability"] = findNumTrial1(None, None)
print(
   f"\nRetrievability = {colouredText(str(round(varDict['Retrieveability'] * 100, 2)), colors.green)}%, Time = {colouredText(str(round(varDict['Original Time'], 2)), colors.green)} days")

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
       f"To reach a retrievability of {colouredText(str(varDict['User Requirement'] * 100), colors.yellow)}%, you must study no longer than {colouredText(round(timeOut * 24, 2), colors.green)} hours, or {colouredText(round(timeOut, 2), colors.green)} days before your test")
else:
   print("You're all good! \nGood luck!")

