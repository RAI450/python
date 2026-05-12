# 16) Palindrome Pyramid
#             1
#            121
#           12321
#          1234321
#         123454321

n=int(input("enter the number"))

for i in range(1,n+1):
    p=1
    q=i-1
    r=(n-i)+1
    s=n+i-1
    for j in range(1,2*n):
        if j<=n:
            if j>=r:
                print(p,end="")
                p+=1
            else:
                print(" ",end="")
        else:
            if j<=s:
                print(q,end="")
                q=q-1
            else:
                print(" ",end="")

    print()
            

            