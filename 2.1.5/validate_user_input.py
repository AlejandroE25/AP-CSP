#   a212_rsa_encrypt.py
import rsa as rsa


def intInput(inputMsg):
    repeats = True
    while repeats:
        inValue = input(inputMsg)

        if not inValue.isdigit() :
            print("Please enter an integer value")
        else:
            repeats = False
            outValue = int(inValue)
            return outValue



#  The isAlpha method checks if a string is comprised of fully alphabetic characters.