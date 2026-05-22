# 7.
# Customer Feedback Analysis System

# An e-commerce company receives thousands of customer reviews every day for its products.

# To analyze customer opinions efficiently, the analytics team wants a Python program that counts how many times each word appears in a review message.

# This helps the company identify frequently used words such as:

# good
# bad
# delivery
# quality
# service

# Write a Python program to count the frequency of every word in a given sentence.

# Input:
# delivery was fast and delivery service was good
# Output:
# delivery : 2
# was : 2
# fast : 1
# and : 1
# service : 1
# good : 1

n=input("enter the sentence: ")

s=n.split()
res=""
for i in s:
    count=0
    if i not in res:
        res+=i+" "
        for j in s:
            if i==j:
                count+=1
        print(i,": ",count)
