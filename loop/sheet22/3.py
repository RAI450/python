# 3) X Star Pattern
#     *   *
#      * *
#       *
#      * *
#     *   *

n=int(input("enter the number "))
y=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i or j==y:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    y-=1