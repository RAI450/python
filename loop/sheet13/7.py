# 7.
#  Prime Sum Lucky Number

# A lottery app checks if sum of digits is prime.

# Write a program to:

# - Find sum of digits
# - If prime print Lucky Number
# - Else Normal Number

# Input:
# 4528

# Output:
# Sum = 19
# Lucky Number

n=int(input("enter the number "))
sum=0

while n>0:
    a=n%10
    sum=sum+a
    n=n//10

print("sum = ",sum)
c=True
for i in range(2,(sum//2)+1):
    
    if sum%i==0:
        print("normal number")
        c=False
        break
if c==True:
    print("lucky number")
    

