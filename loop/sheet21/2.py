# 2)	WAP to print Square, Cube and Square Root of all numbers from 1 to N

n=int(input("enter the number "))

for i in range(1,n+1):
    sqr=i**2
    cube=i**3
    root=float(i**(1/2))
    print("square = ",sqr)
    print("cube = ",cube)
    print("square root = ",root)