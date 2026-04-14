# Assignment 6: Discount Calculator

# Write a Python program that:

# Accepts total amount.
# Calculates 10% discount and final price.

# Input:
# Amount = 1000

# Output:
# Discount = 100
# Final = 900

tot=int(input("enter total amount"))
dis=tot*10/100
print("discount =",dis,"\nfinal =",tot-dis)