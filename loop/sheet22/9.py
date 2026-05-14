# 9) Hollow Diamond Square
#     *****
#     **   **
#     *     *
#     *       *
#     *         *
#     *         *
#     *       *
#     *     *
#     **   **
#     *****

n=int(input("enter the number "))

for i in range(1,n+1):
    a=(n-i)+2
    b=(n+1)+i-2
    if i==1:
        for j in range(1,2*n+1):
            print("*",end="")
        print()

    else:
        for j in range(1,(2*n)+1):
            if j>=a and j<=b:
                print(" ",end="")
            else:
                print("*",end="")
        print()

for i in range(1,n+1):
    a=i+1
    b=(2*n)-i
    if i==5:
        for j in range(1,2*n+1):
            print("*",end="")
        print()
    else:
        for j in range(1,2*n+1):
            if j>=a and j<=b:
                print(" ",end="")
            else:
                print("*",end="")
        print()


        
        

