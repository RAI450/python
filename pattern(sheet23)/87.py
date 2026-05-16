

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

n=int(input("enter the number "))

for i in range(n,0,-1):
    a=i
    b=2*n-i+1
    for j in range(1,2*n+1):
        if j>a and j<b:
            print(" ",end="")
        else:
            print("*",end="")
    print()

for i in range(1,n+1):
    a=i
    b=2*n-i+1
    for j in range(1,2*n+1):
        if j>a and j<b:
            print(" ",end="")
        else:
            print("*",end="")
    print()