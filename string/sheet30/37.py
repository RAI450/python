n=input("enter the string: ")

s=n.split()
res=""
for i in s:
    for j in i[::-1]:
        res+=j
    res+=" "

print(res)