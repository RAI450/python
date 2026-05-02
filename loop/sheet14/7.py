# 7.Alternate Digit Prime Checker

# A math lab adds alternate digits from right side.

# Write a program to:

# - Find sum of alternate digits
# - Check whether sum is Prime or Not

# Input:
# 12345

# Output:
# Alternate Sum = 9
# Not Prime

n=int(input("enter the number "))

sum=0
while n>0:
    a=n%10
    sum=sum+a
    n=n//10
    n=n//10
print("Alternate Sum = ",sum)

for i in range(2,(sum//2)+1):
    if sum%i==0:
        print("not prime")
        break
else:
    print("prime")
