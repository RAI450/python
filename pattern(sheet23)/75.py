
# 123456789
#  1+++++7 
#   1+++5  
#    1+3   
#     1    

n=int(input("enter the number "))
a=2*n-1
for i in range(1,n+1):
    if i==1:
        for j in range(1,2*n):
            print(j,end="")
        print()
        a-=2
    else:
        for j in range(1,2*n):
            if j>=i and j<=(2*n)-i:
                if j==i:
                    print("1",end="")
                elif j==((2*n)-i):
                    print(a,end="")
                    a-=2
                else:
                    print("+",end="")
            else:
                print(" ",end="")
        print()
        
