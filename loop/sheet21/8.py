# 8.

# enter n6
#  654321
#   65432
#    6543
#     654
#      65


n=int(input("enter the number "))
for i in range(1,n):
    x=i-1
    y=n
    for j in range(6,0,-1):
        if x>0:
            print(" ",end="")
            x-=1
        else:
            print(y,end="")
            y-=1
    print()

'''    
n=int(input("enter the number "))

for i in range(n-1):
    for j in range(i):
        print(" ", end='') 
    for k in range(n,i,-1):
        print(k,end='')
    print()

'''























