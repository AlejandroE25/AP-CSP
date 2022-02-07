#   a212_rsa_decrypt.py
import rsa as rsa
from validate_user_input import *

key = intInput("Enter the Key: ")
mod_value = intInput("Enter the Modulus Value: ")
encrypted_msg = input("What message would you like to decrypt (No brackets): ")

#break apart the list that is cut/copied over on ", "
msg = encrypted_msg.split(", ")
print (rsa.decrypt(key,mod_value , msg))
