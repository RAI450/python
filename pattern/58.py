#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5 

n=int(input("enter the number "))

for i in range(n,0,-1):
    a=1
    for j in range(1,n+1):
        if j<i:
            print(" ",end=" ")
        else:
            print(a,end=" ")
            a+=1
    print()