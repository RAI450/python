# 2.Employee Salary Processing
# Store employee salaries in a List and calculate details.

# Requirements:

# Store salaries
# Find average salary
# Display salaries greater than average
# Remove salaries below 15000

# Test Cases:

# Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
# Input: [15000, 15000, 15000] → Average = 15000
# Input: [5000, 7000] → Remaining List = []

m=int(input("enter the number of employees "))
n=[]
for i in range(m):
    s=int(input("enter the salary "+str(i+1)+": "))
    n.append(s)

res=[]
for i in n:
    if i>sum(n)//m:
        print(i)
    if i>=15000:
        res.append(i)

print("average : ",sum(n)//m)
print("remaining list = ",res)



