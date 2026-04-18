# 7. Salary Benefits System
#    A company provides benefits:

# * If salary ≥ 30000 → Eligible for PF
# * If salary ≥ 50000 → Eligible for bonus

# Input:
# Enter salary: 55000

# Output:
# PF applicable
# Bonus applicable

sal=int(input("enter your salary"))

if sal>=30000:
    print("pf applicable")
    if sal>=50000:
        print("bonus applicable")