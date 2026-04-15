# Assignment 1: Restaurant Bill Split

# A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

# Input:
# Total bill amount = 2500
# GST = 5%
# Service charge = 10%
# Number of friends = 4

# Expected Output:
# Final Bill = 2875.0
# Each Person Pays = 718.75

amt,gst,cha,fr=map(int,input("enter total amount,gst,service charge and no. of friends").split())
bill=amt+(amt*cha/100)+(amt*gst/100)
input(F"final bill ={bill} \n each person pays = {bill/fr}")