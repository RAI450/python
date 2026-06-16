# 1.

# =========================================
# ONLINE SHOPPING CART
# ====================

# A shopping website stores purchased products in a dictionary where:
# Key = Product Name
# Value = Quantity Purchased

# Write a program to:

# * Accept a dictionary from the user.
# * Calculate and display the total quantity of products purchased.

# Sample Input:
# {"Laptop":2,"Mouse":3,"Keyboard":1}

# Sample Output:
# Total Quantity = 6

n=int(input("enter the number of products: "))

d={}
for i in range(n):
    k=input("enter the product name: ")
    v=int(input("enter the quantity: "))
    d[k]=v

add=0
for k,v in d.items():
    add+=v

print("total quantity = ",add)

