#   a212_rsa_encrypt.py
import rsa as rsa

while True:
    key = input("Enter the Encryption Key: ")
    while key.isdigit():
        mod_value = input("Enter the Modulus: ")
        while mod_value.isdigit():
            plaintext = input("Enter a message to encrypt: ")
            encrypted_msg = rsa.encrypt(int(key), int(mod_value), plaintext)
            print("Encrypted Message:", encrypted_msg)
            exit()
        if not mod_value.isdigit():
            print("Please enter a valid Modulus")

    if not key.isdigit():
        print("Please input a valid key")

