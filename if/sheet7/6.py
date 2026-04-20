# 6. Company Bonus Distribution System


# A company wants to calculate bonuses for employees based on their years of experience:

# * More than 10 years → 20% bonus
# * 5 to 10 years → 10% bonus
# * 2 to 5 years → 5% bonus
# * Less than 2 years → No bonus

# Write a Python program to calculate the bonus amount.

# Input:
# Enter salary: 50000
# Enter years of experience: 6

# Output:
# Bonus Amount: ₹5000

sal,exp=map(int,input("enter salary and experience ").split())

if exp>10:
    bons=(sal*20)/100
elif exp>=5:
    bons=(sal*10)/100
elif exp>=2:
    bons=(sal*5)/100
else:
    bons="no bonus"

print("Bonus Amount: ",bons)
