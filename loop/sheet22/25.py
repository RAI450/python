# 25) Number Sandglass
#     123454321
#      1234321
#       12321
#        121
#         1
#        121
#       12321
#      1234321
#     123454321

n=int(input("enter the number "))

for i in range(1,n+1):
    a=i
    b=(2*n)-i
    x=1
    y=n-i
              
    for j in range(1,2*n):
        if j>=a and j<=b:
            if j<=n:
                print(x,end="")
                x+=1
            else:
                print(y,end="")
                y-=1
        else:
            print(" ",end="")
    print()

for i in range(1,n):
    a=n-i
    b=n+i

    x=1
    y=i
    for j in range(1,2*n):
        if j>=a and j<=b:
            if j<=5:
                print(x,end="")
                x=x+1
            else:
                print(y,end="")
                y-=1
        else:
            print(" ",end="")
    print()


                

        