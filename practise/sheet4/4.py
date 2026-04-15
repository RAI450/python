# Assignment 4: Travel Distance Calculation

# A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

# Input:
# Speed = 60 km/hr
# Time = 2 hours 30 minutes

# Expected Output:
# Total Time = 2.5 hours
# Distance = 150.0 km

spd,hrs,min=map(int,input("enter speed and time").split())
hrs=hrs+min/60
dis=spd*hrs
print(F"total time ={hrs} hours\n total distance ={dis} km")