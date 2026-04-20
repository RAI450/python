# NOTE: Complete all the following assignments using Nested if-else statements only.

# 1. A bank wants to automate its loan approval process. The system should take salary, 
# credit score, and number of existing loans as input. If the salary is greater than or equal to 30000, 
# then it should check the credit score. If the credit score is greater than or equal to 750,
#  the loan should be approved. Otherwise, it should check the number of existing loans. 
# If the existing loans are less than 2, the loan should be conditionally approved; otherwise, it should be rejected. 
# If the salary is less than 30000, the loan should be rejected. Display the final loan status.

# Input:
# Salary = 40000
# Credit Score = 720
# Existing Loans = 1

# Output:
# Loan Status = Conditional Approval

sal=int(input("enter your salary"))

if sal>=30000:
    cre=int(input("enter your credit score"))
    if cre>=750:
        print("loan status= approved")
    else:
        loan=int(input("enter your existing loans"))
        if loan<2:
            print("loan status= conditional approved")  
        else: print("loan status= rejected")
    
else: print("loan status= rejected")