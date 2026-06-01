n=input("enter the string: ")

res=""
for i in n[::-1]:
    res+=i

print(res)