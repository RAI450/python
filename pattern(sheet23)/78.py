#    1
#   12
#  123
# 1234
#  123
#   12
#    1

n=int(input("enter the number "))

for i in range(1,n+1):
    a=1
    for j in range(1,n+1):
        if j>n-i:
            print(a,end="")
            a+=1
        else:
            print(" ",end="")
    print()
for i in range(n-1,0,-1):
    a=1
    for j in range(1,n+1):
        if j>n-i:
            print(a,end="")
            a+=1
        else:
            print(" ",end="")
    print()