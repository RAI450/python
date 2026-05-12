# 20) Continuous Diamond Numbers
#            1
#           2 3
#          4 5 6
#         7 8 9 10
#          4 5 6
#           2 3
#            1

n=int(input("enter the number "))

cnt=1
for i in range(1,n+1):
    v=n//2+1
    for j in range(1,n+1):
        if j==v
