# 1. Smart Log File Error Pattern Detector

# A cybersecurity company stores server logs containing repeated system activity characters.

# To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

# If multiple substrings have the same length, print the first one found.

#  Input:

# text
# abcabcbb


# Output:

# text
# abc

n=input("enter the string: ")

a=1
l=len(n)
hig=0
t=""
for i in n:
    count=0
    res=i
    for j in range(a,l):
        if n[j] not in res:
            count+=1
            res+=n[j]
        else:
            break
    a+=1
    if count>=hig:
        hig=count
        t=t+res+" "

s=t.split()

org=""
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if count>1:
        org=org+i+" "
org=org.split()
print("text",org[0])
    






