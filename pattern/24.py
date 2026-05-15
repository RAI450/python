# *
# **
# *@*
# *@@*
# * * * * *

n=int(input("enter the number "))

for i in range(1,n+1):
    if i<=n-1:
        for j in range(1,i+1):
            if j==1 or j==i:
                print("*",end="")
            else:
                print("@",end="")
        print()
    else:
        for j in range(1,n+1):
            print("*",end="")