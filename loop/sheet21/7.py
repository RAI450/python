# 7.

# enter n6
#      *
#     **
#    ***
#   ****
#  *****
# ******

n=int(input("enter the number "))

for i in range(1,n+1):
    x=n-i
    for j in range(1,n+1):
        if x>0:
            print(" ",end="")
            x-=1
        else:
            print("*",end="")
    print()
            
