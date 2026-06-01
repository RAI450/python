n=input("enter the string: ")

s=n.split()
res=""
sml=9
for i in s:
    count=0
    for j in i:
        count+=1
    if count<sml:
        sml=count
        res=i
print(res)