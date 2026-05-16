# \     /
#  \   / 
#   \ /  
#    \   
#   / \  
#  /   \ 
# /     \

n=int(input("enter the number "))

for i in range(1,2*n):
    a=i
    b=2*n-i
    for j in range(1,2*n):
        if j==a:
            print("\\",end="")
        elif j==b:
            print("/",end="")
        else:
            print(" ",end="")
    print()
    
