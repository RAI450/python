# 12) Hollow Diamond Numbers
#        1
#       2 2
#      3   3
#     4     4
#      3   3
#       2 2
#        1

n=int(input("enter the number "))

for i in range(1,n+1):            # for input=4
    pre=n-i+1
    aft=n+i-1
    for j in range(1,2*n):
        if j==pre or j==aft:
            print(i,end="")
        else:
            print(" ",end="")
    print()

for i in range(1,n):
    a=1+i
    b=(2*n)-1-i
    c=n-i
    for j in range(1,2*n):
        if j==a or j==b:
            print(c,end="")
        else:
            print(" ",end="")
    print()
