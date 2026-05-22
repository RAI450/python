# 8.
# AI Chat Moderation System

# A social media company is developing an AI-based chat moderation system that analyzes user messages in real time.

# During analysis, the system must identify special symmetric words (palindromes) because they are used as secret tags in internal testing.

# A palindrome word is a word that reads the same forward and backward.

# Write a Python program to find the first palindrome word present in the sentence.

# If no palindrome word exists, print:

# No palindrome word found
# Input:
# madam and arun went to level racecar station
# Output:
# madam

n=input("enter the sentence: ")

nrev=""
s=n.split()
l=len(s)
for i in s:
    rev=""
    for j in i:
        rev=j+rev
    nrev=nrev+rev+" "
nrev=nrev.split()

for i in range(l):
    if s[i]==nrev[i]:
        print(s[i])
        break
else:
    print("no palindrome word found")