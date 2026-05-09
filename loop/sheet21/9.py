# 9.
#     1
#    10
#   101
#  1010
# 10101

n=int(input("enter the number "))

for i in range(1,n+1):
    x=n-i
    t=True
    for j in range(1,n+1):
        if x>0:
            print(" ",end="")
            x-=1
        else:
            if t==True:
                print("1",end="")
                t=False
            else:
                print("0",end="")
                t=True
    print()