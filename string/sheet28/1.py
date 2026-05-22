# 1.Find the Longest Substring Without Repeating Characters
# Cybersecurity Session Tracking System

# A cybersecurity company monitors user session IDs generated during secure login sessions.

# To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

# Input:
# abcabcbb
# Output:
# abc


n=input("enter the string: ")

l=len(n)
a=0
hig=0
rep=""
for i in n:
    res=i
    a+=1
    count=0
    for j in range(a,l):
        if n[j]!=i and n[j] not in res:
            count+=1
            res=res+n[j]
        else:
            if count>hig:
                hig=count
                rep=res
            break
print(rep)




