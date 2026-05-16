#     #    
#    *#*   
#   **#**  
#  ***#*** 
# ****#****

n=int(input("enter the number "))

for i in range(1,n+1):
    a=n-i+1
    b=n+i-1
    for j in range(1,2*n):
            if j>=a and j<=b:
                if j==n:
                    print("#",end="")
                else:
                    print("*",end="")
            else:
                print(" ",end="")
    print()