n=input("enter the string: ")

s=n.split()
res=""
for i in s[::-1]:
    res+=i+" "

print(res)