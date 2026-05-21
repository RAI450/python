# 5. Website URL Verification System

# A software company is developing an automated website registration
# portal. Before saving a website address, the system must verify whether
# the URL follows the required company format.

# Conditions: - Must start with www - Must end with .com

# Input: Enter website: www.amazon.com

# Output: Valid Website

n=input("Enter website: ")

l=len(n)
flag=1
for i in range(3):
    if n[i]!="w":
        flag=0
        break
else:
    if n[l-4:l]!=".com":
        flag=0
if flag==0:
    print("invalid website")
else:
    print("valid website")



