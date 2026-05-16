#     1    
#    123   
#   12345  
#  1234567 
# 123456789

n=int(input("enter the number "))

for i in range(1,n+1):
    a=n-i+1
    b=n+i-1
    x=1
    for j in range(1,2*n):
        if j>=a and j<=b:
            print(x,end="")
            x+=1
        else:
            print(" ",end="")
    print()