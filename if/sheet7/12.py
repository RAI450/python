# 12. Restaurant Bill with GST System

# A restaurant applies GST based on the total bill amount:

# * Up to ₹1000 → 5% GST
# * ₹1001 to ₹5000 → 12% GST
# * Above ₹5000 → 18% GST
#   Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

# Write a Python program to calculate the final bill.

# Input:
# Enter bill amount: 4000

# Output:
# Final Bill Amount: ₹4680

amt=int(input("Enter bill amount: "))
if amt<=1000:
    gst=(amt*5)/100
elif amt<=5000:
    gst=(amt*12)/100
else:
    gst=(amt*18)/100
if amt>3000:
    gst=gst+200

print("Final Bill Amount: ",amt+gst)