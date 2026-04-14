# Assignment 12: Change Return System

# Write a Python program that:

# Accepts amount.
# Calculates ₹100, ₹50, ₹10 notes.

# Input:
# Amount = 380

# Output:
# ₹100 x 3
# ₹50 x 1
# ₹10 x 3

amt=int(input("enter amount"))
h=int(amt/100)
f=int((amt-(h*100))/50)
t=int((amt-(h*100)-(f*50))/10)
print("₹100 x",h,"\n₹50 x",f,"\n₹10 x",t)