# 55555
#  4444
#   333
#    22
#     1

n=int(input("enter the number "))
a=n
for i in range(1,n+1):
    
    for j in range(1,n+1):
        if j>=i:
            print(a,end="")
            
        else:
            print(" ",end="")
    a-=1
    print()