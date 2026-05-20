# 4.
# Employee ID Validator

# A company wants to validate employee IDs before storing them in the database.

# Conditions:
# - ID must start with "EMP"
# - Total length should be 8
# - Remaining characters should be digits only

# Input:
# Enter Employee ID: EMP10234

# Output:
# Valid Employee ID

n=input("Enter Employee ID: ")

count=0
chr=0
for i in n:
    count+=1
    if ord(i)>=65 and ord(i)<=90:
        chr+=1
flag=1
if count==8 and chr==3:
    if n[0]=="E" and n[1]=="M" and n[2]=="P":
        for i in range(3,count):
            print(ord(n[i]))
            if ord(n[i])<48 or ord(n[i])>57:
                flag=0
        if flag==0:
            print("invalid employee id")
        else:
            print("valid employee id")
    else:
        print("invalid employee id ")
else:
    print("invalid employee id")


