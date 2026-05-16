#     1
#    22
#   333
#  4444
# 55555

n=int(input("enter the number "))
a=1
for i in range(n,0,-1):
    
    for j in range(1,n+1):
        if j<i:
            print(" ",end="")
        else:
            print(a,end="")
    a+=1        
    print()