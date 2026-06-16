# 11.

# =========================================
# PRODUCT SALES ANALYSIS
# ======================

# sales = [
# "Mobile",
# "Laptop",
# "Mobile",
# "Tablet",
# "Laptop",
# "Mobile"
# ]

# Write a program to:

# * Count sales of each product.
# * Display products in sorted order.

# Sample Output:
# Laptop : 2
# Mobile : 3
# Tablet : 1

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

s={}
for x in sales:
    s[x]=s.get(x,0)+1

for k,v in sorted(s.items()):
    print(k," ",v)
