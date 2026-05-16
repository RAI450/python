# x
# xx
# xxx
# xxxx
# xxx
# xx
# x

n=int(input("enter the number "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print("x",end="")
        else:
            print(" ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n+1):
        if j<=i:
            print("x",end="")
        else:
            print(" ",end="")
    print()

