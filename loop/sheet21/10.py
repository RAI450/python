# 10.

# enter number6
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

n=int(input("enter the number "))

for i in range(1,n):
    for j in range(0,i):
        print(j,end=" ")
    print()