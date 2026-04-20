# 13. Employee Performance Appraisal System


# A company evaluates employees based on performance rating (1–5):

# * 5 → 25% salary hike
# * 4 → 20% salary hike
# * 3 → 10% salary hike
# * 2 → 5% salary hike
# * 1 → No hike
#   If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

# Write a Python program to calculate revised salary.

# Input:
# Enter salary: 18000
# Enter rating: 4

# Output:
# Revised Salary: ₹23600

sal,rate=map(int,input("enter salary and rating(1-5)").split())
if rate==5:
    hike=(sal*25)/100
elif rate==4:
    hike=(sal*20)/100
elif rate==3:
    hike=(sal*10)/100
elif rate==2:
    hike=(sal*5)/100
else:
    hike=0
if sal<20000 and rate>=4:
    hike=hike+2000
print("Revised Salary: ",sal+hike)
