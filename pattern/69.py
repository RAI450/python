# *********
#  ******* 
#   *****  
#    ***   
#     *    

n=int(input("enter the number "))
a=1
b=2*n-1
for i in range(1,n+1):
    for j in range(1,2*n):
        if j>=a and j<=b:
            print("*",end="")
        else:
            print(" ",end="")
    a+=1
    b-=1
    print()
