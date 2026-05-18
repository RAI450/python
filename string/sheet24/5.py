# 5.
# Advanced Password Security Checker

# A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

# Conditions: Password must:

# Start with an uppercase letter
# End with a digit
# Contain at least 2 digits
# Contain at least 1 special character (@ # $ % & *)
# Must not contain spaces
# Length should be between 8 and 15 characters

# Input: Enter password: Python@45

# Output: Secure Password


p = input("Enter password: ")

digit = 0
special = 0

for i in p:
    
    if i.isdigit():
        digit += 1
    
    if i=="@" or i=="#" or i=="$" or i=="%" or i=="&" or i=="*":
        special += 1

if (len(p) >= 8 and len(p) <= 15 and
    p[0].isupper() and
    p[-1].isdigit() and
    digit >= 2 and
    special >= 1 and
    " " not in p):
    
    print("Secure Password")

else:
    print("Invalid Password")