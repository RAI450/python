# 123456789
#  1234567 
#   12345  
#    123   
#     1  

n=int(input("enter the number "))
a=1
b=2*n-1
for i in range(1,n+1):
    x=1
    for j in range(1,2*n):
        if j>=a and j<=b:
            print(x,end="")
            x+=1
        else:
            print(" ",end="")
    a+=1
    b-=1
    print()