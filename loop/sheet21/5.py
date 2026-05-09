# 5)

# A
# AB
# ABC
# ABCD
# ABCDE

n=int(input("enter the number "))

for i in range(1,n+1):
    x=65
    for j in range(1,i+1):
        print(chr(x),end=" ")
        x+=1
    print()