# 12.
# =============================
# ONLINE FOOD DELIVERY ANALYSIS
# =============================

# orders = [
# "Pizza",
# "Burger",
# "Pizza",
# "Pasta",
# "Burger",
# "Pizza",
# "Pasta"
# ]

# Write a program to:

# * Count orders of each food item.
# * Find the most ordered item.

# Sample Output:
# Pizza : 3
# Burger : 2
# Pasta : 2

# Most Ordered : Pizza

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

ord={}
for w in orders:
    ord[w]=ord.get(w,0)+1

max=0
high=""
for k,v in ord.items():
    print(k," : ",v)
    if v>max:
        max=v
        high=k
print("most ordered : ",high)



