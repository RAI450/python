# 3)	WAP to find out all the leap years between two entered years

n1=int(input("enter the number "))
n2=int(input("enter the number "))

for i in range(n1,n2+1):
    if (i%400==0) or (i%4==0 and i%100!=0):
        print(i)
