# 5) Number-Star Palindrome
#     12344321
#     123**321
#     12****21
#     1****1

n=int(input("enter the number "))

for i in range(1,n+1):
    a=n-i+2
    b=n-i+1
    for j in range(1,n+1):
        if j>=a:
            print("*",end="")
        else:
            print(j,end="")
    for j in range(n,0,-1):
        if j>b:
            print("*",end="")
        else:
            print(j,end="")
    print()




