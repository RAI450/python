# 10) Slanted Star Block
#     **
#      **
#       **
#        **

n=int(input("enter the number "))

for i in range(1,n+1):
    a=i
    b=i+1
    for j in range(1,b+1):
        if j==a or j==b:
            print("*",end="")
        else:
            print(" ",end="")
    print()