# 9. Smart Loan Eligibility System
# A bank approves loans based on salary, age, credit score, and EMI.

# If salary is 40000 or above, then check age. If age is between 21 and 60, then check credit score.
# If credit score is 750 or above, then check EMI. If EMI is less than or equal to 40% of salary, approve at 8%; otherwise approve at 10%.
# If credit score is below 750, then check if it is at least 650. If yes, approve at 12%; otherwise reject.

# If salary is below 40000, then check if salary is at least 25000 and credit score is at least 700. If yes, approve at 13%; otherwise reject.

# Input:
# Salary = 50000
# Age = 30
# Credit Score = 760
# EMI = 18000

# Output:
# Loan Status = Approved at 8%

sal=int(input("enter salary "))
age=int(input("enter age "))
cre=int(input("enter credit score "))
emi=int(input("enter emi "))

if sal>=40000:
    if age>=21 and age<=60:
        if cre>=750:
            if emi<=(40*sal)/100:
                print("approved at 8%")
            else:
                print("approved at 10%")
        elif cre>=650:
            print("approved at 12%")
        else:
            print("rejected")
elif sal>=25000 and cre>=700:
    print("approved at 13%")
else:
    print("rejected")
