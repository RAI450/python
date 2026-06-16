# 6.
# NOTE: using tuple only
# An electronics store wants to maintain product information. Since product details should not be modified accidentally,
#  each product record is stored as a tuple.

# Tuple Format:

# (product_id, product_name, price)

# Requirements:

# Read N product details from the user and store them as tuples in a list.
# Display all product details.
# Find and display the costliest product.
# Find and display the cheapest product.
# Calculate and display the average price of all products.
# Display all products whose price is greater than ₹50,000.

# Test Case:

# Input:

# Enter number of products: 4

# P101 Laptop 65000
# P102 Mobile 25000
# P103 Television 80000
# P104 Tablet 30000

# Expected Output:

# All Products:
# ('P101', 'Laptop', 65000)
# ('P102', 'Mobile', 25000)
# ('P103', 'Television', 80000)
# ('P104', 'Tablet', 30000)

# Costliest Product:
# ('P103', 'Television', 80000)

# Cheapest Product:
# ('P102', 'Mobile', 25000)

# Average Price:
# 50000.0

# Products Above ₹50,000:
# ('P101', 'Laptop', 65000)
# ('P103', 'Television', 80000)

n=int(input("enter the number of products"))

rec=[]
for i in range(1,n+1):
    id=input("enter the id: ")
    name=input("enter the name: ")
    price=int(input("enter the price: "))
    s=(id,name,price)
    rec.append(s)

bda=rec[0]
chota=rec[0]
add=0
hc=[]
for i in rec:
    print(i)
    add+=i[2]
    if i[2]>bda[2]:
        bda=i
    if i[2]<chota[2]:
        chota=i
    if i[2]>50000:
        hc.append(i)

print("costliest price: ",bda)
print("cheapest price: ",chota)
print("average price: ",add/n)

for i in hc:
    print(i)