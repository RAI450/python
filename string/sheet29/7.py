# # 7. Enterprise Password Pattern Strength Analyzer

# A cybersecurity company wants to validate advanced passwords.

# ## Conditions:
# * Minimum 10 characters
# * At least:

#   * 1 uppercase letter
#   * 1 lowercase letter
#   * 1 digit
#   * 1 special character
# * No consecutive repeating characters
# * No spaces allowed

# ### Input:
# text
# Pyth@n1234

# ### Output:
# text
# Strong Password

# ### Input:
# text
# Paaass@12

# ### Output:
# text
# Weak Password

n=input("enter the password: ")

a=""
l=len(n)
flag=1
upper=0
lower=0
digit=0
spec=0
for i in n:
    if l<10 or i==" " or a==i:
        flag=0
        break

    if ord(i)>=65 and ord(i)<=90:
        upper+=1
    elif ord(i)>=97 and ord(i)<=122:
        lower+=1
    elif ord(i)>=48 and ord(i)<=57:
        digit+=1
    else:
        spec+=1
    a=i
    
if flag==1 and upper>0 and lower>0 and digit>0 and spec>0:
    print("strong password")
else:
    print("weak password")