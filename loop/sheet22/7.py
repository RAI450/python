# 7) Reverse Number Triangle
#     - - - -
#     2 - - -
#     4 3 - -
#     6 5 4 -
#     8 7 6 5

n=int(input("enter the number "))
count=0

for i in range(1,n+1):
    a=i-1
    p=i+count
    if i==1:
        for j in range(1,n):
            print("-",end=" ")
        print()
    else:
        count=0
        for j in range(1,n):
            if j>a:
                print("-",end=" ")
            else:
                print(p,end=" ")
                count+=1
                p-=1
        print()