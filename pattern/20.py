# 1
# 12
# 1 3
# 1  4
# 12345

n=int(input("enter the number "))

for i in range(1,n+1):
    if i<=n-1:
        for j in range(1,i+1):
            if j==1 or j==i:
                print(j,end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,n+1):
            print(j,end="")