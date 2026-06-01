# 4.
# Palindrome Number List Checker
# Scenario

# A system checks lucky numbers which are palindromes.

# Requirements
# Check palindrome numbers
# Store palindrome numbers in list
# Count palindrome numbers
# Find largest palindrome
# Sort palindrome list
# Test Cases

# Input:
# [121, 131, 20, 44, 55, 100]

# Output:

# Palindromes: [121, 131, 44, 55]
# Count: 4
# Largest: 131
# Sorted: [44, 55, 121, 131]

m=int(input("enter the number of integers "))
n=[]
for i in range(m):
    s=int(input("enter the integers "+str(i+1)+": "))
    n.append(s)

pal=[]
for i in n:
    a=""
    for j in str(i)[::-1]:
        a=a+j
    if str(i)==a:
        pal.append(i)

print(pal)
print("count ",len(pal))
print("largest : ",max(pal))
pal.sort()
print("sorted: ",pal)

