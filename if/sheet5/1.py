# 1. Smart Voting & ID Verification System
#    A government system verifies whether a citizen can vote and whether they have a valid ID.

# * If age ≥ 18 → Eligible to vote
# * If ID proof is available → Allowed inside booth

# Input:
# Enter age: 22
# Do you have ID (yes/no): yes

# Output:
# Eligible to vote
# Allowed inside booth

age=int(input("enter your age"))

if age<18:
    print("not eligible to vote")

if age>=18:
    id=input("Do you have ID (yes/no):")
    print("eligible to vote")
    if id=="yes":
        print("allowed inside booth")
    if id=="no":
        print("not allowed")

