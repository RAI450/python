# 6)

# a
# ab
# abc
# abcd
# abcde

n=int(input("enter the number "))

for i in range(1,n+1):
    x=97
    for j in range(1,i+1):
        print(chr(x),end=" ")
        x+=1
    print()