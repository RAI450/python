# 6. Find Occurrence of a Word in a String

# Product Review Analysis System

# An e-commerce company wants to analyze customer reviews.

# The company wants a Python program to count how many times a particular word appears in a review.

# Input Sentence:
# iphone is good and iphone battery is strong
# Word:
# iphone
# Output:
# 2

n=input("enter the password: ")

n=input("enter the sentence: ")
w=input("enter the word: ")

count=0
s=n.split()
for i in s:
    if i==w:
        count+=1
print(count)