n=input("enter the string: ")

s=n.split()

for i in s:
    res=""
    for j in i[::-1]:
        res+=j
    if i==res:
        print(i)
        break