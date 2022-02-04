##############################################################################
# a215_security_checklist.py
##############################################################################

print("Let's check your security. Answer y or n to each of the questions.")

phish = input("Can you recognize phishing emails? ")
pw = input("Is your password strong? ")
auth = input("Do you use multi-factor authentication? ")
enc = input("Do you know how to encrypt sensitive information? ")

if phish or pw or auth or enc == 'n':
    print("You can improve your security habits.")

else:
    print("You have good security habits")
