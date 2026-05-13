# 27) Continuous Number Pyramid
#             1
#            2 3
#           4 5 6
#          7 8 9 10

n=int(input("enter the number "))
cnt=1

for i in range(1,n+1):
    if i%2==0:
        next=n+i-1
        prev=n-i+1
        for j in range(1,2*n):
            if j>=prev and j<=next:
                if j%2!=0:
                    print(cnt,end="")
                    cnt+=1
                else:
                    print(" ",end="")
            else:
                print(" ",end="")
        print()
    else:
        next=n+i-1
        prev=n-i+1
        for j in range(1,2*n):
            if j>=prev and j<=next:
                if j%2==0:
                    print(cnt,end="")
                    cnt+=1
                else:
                    print(" ",end="")
            else:
                print(" ",end="")
        print()


