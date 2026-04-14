# Assignment 11: Time Duration Adder

# Write a Python program that:

# Accepts hours, minutes, seconds.
# Converts into total seconds.

# Input:
# Hours = 1
# Minutes = 2
# Seconds = 30

# Output:
# Total Seconds = 3750

h,m,s=map(int,input("enter hours ,minutesand seconds").split())
sec=(h*3600)+(m*60)+s
print("total seconds =",sec)
