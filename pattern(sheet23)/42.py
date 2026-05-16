# 54321
# 5432
# 543
# 54
# 5

n=int(input("enter the number "))

for i in range(1,n+1):
    a=n
    for j in range(1,(n-i)+2):
        print(a,end="")
        a-=1
    print()