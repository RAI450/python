n=input("enter the string: ")

res=""
s=n.split()
for i in s:
    if i not in res:
        res+=i+" "
print(res)