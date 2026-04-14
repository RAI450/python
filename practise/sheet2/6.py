# Assignment 6: Smart Coin Machine
# ========================================

# You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

# Write a Python program that:
# - Accepts the total amount.
# - Calculates how many ₹10 coins and ₹5 coins will be dispensed.
# - Displays the result.

# Example:
# Amount = ₹35
# Output = ₹10 x 3, ₹5 x 1

amt=int(input("total amount - "))
ten=int(amt/10)
five=int((amt-(ten*10))/5)
print("amount = ",amt)
print("₹10 x ",ten,", ₹5 x",five)