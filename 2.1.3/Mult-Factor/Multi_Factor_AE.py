# a213_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restricted app
my_auth = mfg.MultiFactorAuth()

# set the users authentication information
question = "What is your favourite German word?"
answer = "Backpfeifengesicht"
my_auth.set_authentication(question, answer)
password = "KwintinLikesTurtlesNamedKyle"

my_auth.set_authorization(pw=password)

# start the GUI
my_auth.mainloop()
