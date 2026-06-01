n=input("enter the string: ")

flag=1
for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
        if count>1:
            break
    if count>1:
        flag=0
        break
print(bool(flag))