# 11) Butterfly Number Pattern
#     1      1
#     12    21
#     123  321
#     12344321
#     123  321
#     12    21
#     1      1

n=int(input("enter the number "))

for i in range(1,n+1):
    a=i
    b=2*n-i+1
    e=i
    for j in range(1,(2*n)+1):
        if j<=a:
            print(j,end="")
        elif j>=b:
            print(e,end="")
            e-=1
        else:
            print(" ",end="")
    print()

for i in range(1,n+1):
    a=n-i
    b=n+i+1
    e=n-i
    for j in range(1,(2*n)+1):
        if j<=a:
            print(j,end="")
        elif j>=b:
            print(e,end="")
            e=e-1
        else:
            print(" ",end="")
    print()



 

