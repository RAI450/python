# 7.Factory Production – Factorial Expansion List

# Problem Statement
# A factory produces items where production capacity is defined using factorial growth.
# Given a list of numbers, replace each number with its factorial value.

# Then perform analysis on the resulting list.

# Tasks:
# Convert each element to factorial
# Find sum of all factorial values
# Find maximum factorial value
# Count how many factorial values are even

# Input:
# A list of integers

# Example 1
# Input:
# [3, 4, 5]

# Processing:
# 3! = 6
# 4! = 24
# 5! = 120

# Output:
# [6, 24, 120]
# Sum = 150
# Max = 120
# Even Count = 3

m=int(input("enter the number of integers "))
n=[]
for i in range(m):
    s=int(input("enter the integers "+str(i+1)+": "))
    n.append(s)

for i in range(len(n)):
    pro=1
    for j in range(1,n[i]+1):
        pro=pro*j
    n[i]=pro

print(n)
add=0
count=0
max=0
for i in n:
    add=add+i
    if i%2==0:
        count+=1
    if i>max:
        max=i
print("sum =",add)
print("max =",max)
print("even count =",count)

