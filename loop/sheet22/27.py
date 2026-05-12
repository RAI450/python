# 27) Continuous Number Pyramid
#             1
#            2 3
#           4 5 6
#          7 8 9 10

n=int(input("enter the number "))
cnt=1

for i in range(1,4):
    next=n+i-1
    prev=n-i+1
    for j in range(1,2*n):
        k=j
        if k<=next and k>=prev:
            print(cnt,end="")
            cnt+=1                       # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            k=k+2
        else:
            print(" ",end="")
    print()

