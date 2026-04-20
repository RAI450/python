# 14. Online Course Fee System

# An online platform offers courses with fixed fees:

# * Programming → ₹5000
# * Design → ₹4000
# * Marketing → ₹3000
#   Discount is applied based on user type:
# * Student → 20% discount
# * Working Professional → 10% discount
# * Others → No discount

# Write a Python program to calculate final course fee.

# Input:
# Enter course category: Programming
# Enter user type: Student

# Output:
# Final Course Fee: ₹4000

cat=input("Enter course category: ")
user=input("Enter user type: ")

if cat=="programming":
    amt=5000
elif cat=="design":
    amt=4000
elif cat=="marketing":
    amt=3000
if user=="student":
    dis=(amt*20)/100
elif user=="working professional":
    dis=(amt*10)/100
else:
    dis=0
print("Final Course Fee: ",amt-dis)

