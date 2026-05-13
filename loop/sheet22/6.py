# 6) Number Triangle with Dashes
#     - - - - 1
#     - - - 2 3
#     - - 3 4 5
#     - 4 5 6 7
#     5 6 7 8 9

n=int(input("enter the number "))


for i in range(1,n+1):
    a=n-i
    b=i
    for j in range(1,n+1):
        if j<=a:
            print("-",end="")
        else:
            print(b,end="")
        b+=1
    print()
