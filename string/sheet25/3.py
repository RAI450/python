# 3.
# Word Counter in Complaint Message

# A customer care system wants to count how many words are present in a complaint message.

# Input:
# Enter complaint: Delivery was delayed again today

# Output:
# Total words: 5

n=input("enter complaint: ")

count=0
a=ord(n[0])
if (a>=65 and a<=90) or (a>=97 and a<=122):
    count=1
c=""
for i in n:
    b=ord(i)
    if (b>=65 and b<=90) or (b>=97 and b<=122) and c==" ":
        count+=1
    c=i
print("total words: ",count)    