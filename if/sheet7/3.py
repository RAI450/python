# 3. Income Tax Department System

# The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

# * Up to ₹2,50,000 → No tax
# * ₹2,50,001 to ₹5,00,000 → 5% tax
# * ₹5,00,001 to ₹10,00,000 → 20% tax
# * Above ₹10,00,000 → 30% tax

# Write a Python program to calculate the tax amount.

# Input:
# Enter annual income: 800000

# Output:
# Tax Payable: ₹110000
# ---------------------------------------------------------------------------------------------------
income=int(input("Enter annual income"))

# if income<=250000:
#     tax=0
# elif income<=500000:
#     tax=(income*5)/100
# elif income<=1000000:
#     tax=(income*20)/100
# else:
#     tax=(income*30)/100

# print("tax payable: ",tax)

#slab-wise tax-------------------------------------------
# First ₹2,50,000 → No tax = ₹0
# Next ₹2,50,000 (2.5L to 5L) → 5% = ₹12,500
# Remaining ₹3,00,000 (5L to 8L) → 20% = ₹60,000

if income<=250000:
    tax=0
elif income<=500000:
    tax=((income-250000)*5)/100
elif income<=1000000:
    tax=(((income-500000)*20)/100)+((250000*5)/100)
else:
    tax=((250000*5)/100) + ((500000*20)/100) + (((income-1000000)*30)/100)

print("tax payable: ",tax)