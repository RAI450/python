# Assignment 9: Fuel Cost Calculator

# Write a Python program that:

# Accepts distance (km), mileage (km/litre), and petrol price.
# Calculates total fuel cost.

# Input:
# Distance = 100
# Mileage = 20
# Petrol Price = 100

# Output:
# Cost = 500


d,m,p=map(int,input("enter distance,mileage,petrol price").split())
cost =(d/m)*p
print("cost =",cost)