# 8.
# =========================================
# LIBRARY BOOK ISSUE TRACKER
# ==========================

# A library records issued books.

# books = [
# "Python",
# "Java",
# "Python",
# "C++",
# "Java",
# "Python"
# ]

# Write a program to:

# * Count how many times each book was issued.

# Sample Output:
# {
# 'Python':3,
# 'Java':2,
# 'C++':1
# }

books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]

b={}
for x in books:
    b[x]=b.get(x,0)+1

for k,v in b.items():
    print(k," : ",v)