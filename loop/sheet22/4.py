# 4) Vertical Diamond
#        *
#       * *
#      *   *
#     *     *
#      *   *
#       * *
#        *

n=int(input("enter the number "))

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
    #    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


