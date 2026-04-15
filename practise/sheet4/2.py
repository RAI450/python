# Assignment 2: Mobile EMI Calculation

# You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

# Input:
# Mobile price = 30000
# Down payment = 5000
# Interest rate = 10%
# Months = 10

# Expected Output:
# Remaining Amount = 25000
# Total with Interest = 27500
# Monthly EMI = 2750.0

pri,down,rate,mon=map(int,input("enter price,down payment,intrest rate,months").split())
rem=pri-down
total=rem+(rem*10/100)
print(F"remaining amount = {rem} \n total with intrest = {total}\n monthly emi = {total/10}")