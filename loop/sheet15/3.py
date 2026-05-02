# 3.Fibonacci Population Growth Tracker

# A wildlife research team is studying the growth of a rare species.  
# They observe that the population follows a Fibonacci pattern:

# - Month 1 → 0 animals  
# - Month 2 → 1 animal  
# - Every next month → sum of previous two months  

# The researchers want to analyze the growth pattern.

# Write a program to:

# - Read number of months n
# - Generate Fibonacci series up to n months using loop
# - Print population for each month
# - Find total population observed
# - Count how many months population exceeded 5

# Input:
# 8

# Output:
# Population Growth:
# 0 1 1 2 3 5 8 13

# Total Population = 33
# Months with Population > 5 = 2

n=int(input("enter the months"))

a=0
b=1
s="0"+" "+"1"
sum=1
count=0
for i in range(3,n+1):
    temp=a+b
    sum+=temp
    a=b
    b=temp
    s=s+" "+str(temp)
    if temp>5:
        count+=1
print("population growth :",s)
print("total population = ",sum)
print("months with population > 5 = ",count)