#    *   
#   *_*  
#  *_*_* 
# *_*_*_*
#  *_*_* 
#   *_*  
#    *

n=int(input("enter the number "))

for i in range(1,n+1):
    a=n-i+1
    b=n+i-1
    if i%2==0:
        for j in range(1,(2*n)):
            if j>=a and j<=b:
                if j%2==0:
                    print("_",end="")
                else:
                    print("*",end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,(2*n)):
            if j>=a and j<=b:
                if j%2==0:
                    print("*",end="")
                else:
                    print("_",end="")
            else:
                print(" ",end="")
        print()

for i in range(1,n):
    a=i+1
    b=2*n-i-1
    if i%2==0:
        for j in range(1,2*n):
            if j>=a and j<=b:
                if j%2==0:
                    print("_",end="")
                else:
                    print("*",end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,2*n):
            if j>=a and j<=b:
                if j%2==0:
                    print("*",end="")
                else:
                    print("_",end="")
            else:
                print(" ",end="")
        print()



