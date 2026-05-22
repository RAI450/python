# 2.
# Find the Most Frequently Occurring Word
# News Channel Keyword Analyzer

# A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

# Write a Python program to find the word with the highest frequency.

# Input:
# india won the match and india created history
# Output:
# india

n=input("enter the sentence: ")

s=n.split()
l=len(s)
hig=0
fre=""
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if count>hig:
        hig=count
        fre=i
print(fre)