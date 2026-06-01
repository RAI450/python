n=input("enter the string: ")
w=input("enter the word: ")

s=n.split()
count=0
for i in s:
    if i==w:
        count+=1
print(count)