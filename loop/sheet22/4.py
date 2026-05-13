# 4) Vertical Diamond
#        *
#       * *
#      *   *
#     *     *
#      *   *
#       * *
#        *

n=int(input("enter the number "))

a=2
b=n-1
for i in range(1,n+1):
    if i<=(n//2)+1:
        prev=((n//2)+1)-i+1
        next=((n//2)+1)+i-1
        for j in range(1,n+1):
            if j==prev or j==next:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,n+1):
            if j==a or j==b:
                print("*",end="")
            else:
                print(" ",end="")
        a=a+1
        b=b-1
        print()
                


