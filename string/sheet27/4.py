# 4. Program should work for both uppercase and lowercase letters.

#  Find the Shortest Word in a Sentence

# Telecom SMS Cost Optimization System

# A telecom company charges customers based on the length of words used in bulk SMS campaigns.

# The company wants to identify the shortest word in every message for analytics purposes.

# Write a Python program to find the shortest word from a given sentence.

# Input:


# Python is very easy to learn


# Output:


# is

n=input("enter the sentence: ")

s=n.split()
ind=0
word=0
shrt=len(s[0])

for i in s:
    count=0
    word+=1
    for j in i:
        count+=1
        if count<shrt:
            shrt=count
            ind=word
print(s[ind])
            


