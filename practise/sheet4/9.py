# Assignment 9: Petrol Cost Calculation

# You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

# Input:
# Distance = 450 km
# Mileage = 15 km/litre
# Petrol price = 110/litre

# Expected Output:
# Petrol Used = 30.0 litres
# Total Cost = 3300.0

dis,mil,pri=map(int,input("enter distance ,mileage,petrol price").split())
used= dis/mil
cost= used*pri
print(F"petrol used ={used} litres\ntotal cost ={cost}")