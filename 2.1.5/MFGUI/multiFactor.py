# a215_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restircted app
shouldRepeat = True

while shouldRepeat:
    user = input("Enter in a valid username:  ")
    for c in user:
        if user.isalnum:
            shouldRepeat = False
        else:
            print("Please only use Alpha numeric characters")
        
shouldRepeat = True

while shouldRepeat:
    password = input("Enter in a valid password:  ")
    for c in password:
        if user.isalnum:
                shouldRepeat = False
        else:
            print("Please only use Alpha numeric characters")

print("\nAll done!")

        
my_auth = mfg.MultiFactorAuth() # Creates a local variable for the class MultiFactorAuth


my_auth.set_authorization(user, password) # Sets the login information using the set_authorization function
# confirm authorization info
auth_info = my_auth.get_authorization() # Returns the Authorization info
print(auth_info)

# set the users authentication information
question = "What is your favorite color?" # Set the security question
answer = "purple" # Set the answer
my_auth.set_authentication(question, answer)  # Officially set the questio and answer

# start the GUI
my_auth.mainloop()
