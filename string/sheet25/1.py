# Email Username Validator

# A company wants to check whether an employee email username is valid before creating an official account.

# Conditions:
# - Username should start with a letter
# - Username can contain letters, digits, underscore (_)
# - No spaces allowed
# - Length should be between 5 and 12 characters

# Input:
# Enter username: ajay_123

# Output:
# Valid Username

n=input("enter username: ")

count=0
spc=0
a=ord(n[0])
if (a>=65 and a<=90) or (a>=97 and a<=122):
    for i in n:
        b=ord(i)
        if (b>=65 and b<=90) or (b>=97 and b<=122) or (b>=49 and b<=57):
            count+=1
        elif i=="_":
            spc+=1
        else:
            print("invalid username ")
            break
else:
    print("invalid username ")

if count<5 and count>12:
    print("invalid username")
else:
    print("valid username ")


