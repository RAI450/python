# 3.
# Character Occurrence Checker in Product Review

# An e-commerce website wants to know how many times a particular character appears in a product review.

# Input: Enter product review: this product is really good Enter character to check: o

# Output: Character 'o' occurs: 3 times           

n=input("Enter product review: ").lower()
c=input("Enter character to check: ").lower()

cr=0
for i in n:
    if i==c:
        cr+=1
print("Total character: ",cr)