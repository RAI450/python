# 4. E-Commerce Discount Engine


# An online shopping platform provides discounts to customers based on their total purchase amount:

# * Above ₹5000 → 20% discount
# * ₹2000 to ₹5000 → 10% discount
# * Below ₹2000 → 5% discount

# Write a Python program to calculate the final amount after discount.

# Input:
# Enter purchase amount: 4500

# Output:
# Final Amount: ₹4050

amt=int(input("Enter purchase amount: "))

if amt>5000:
    dis=(amt*20)/100
elif amt>=2000:
    dis=(amt*10)/100
else:
    dis=(amt*5)/100

print("Final Amount: ",amt-dis)