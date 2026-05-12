# 26) Right Hollow Number Triangle
#     1
#     12
#     1 3
#     1  4
#     12345

n=int(input("enter the number "))

s=1
k=1
for i in range(1,n+1):
    if i<n:
        for j in range(1,i+1):
            if j==k or j==s:
                print(j,end="")
            else:
                print(" ",end="")
        k+=1
        print()
    else:
        for j in range(1,n+1):
            print(j,end="")
            

