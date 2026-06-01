n=input("enter the string: ")

for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
        if count>1:
            break
    else:
        print(i)
        break
