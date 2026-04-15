# Assignment 7: Cricket Run Rate

# In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

# Input:
# Total runs = 275
# Overs = 48.3

# Expected Output:
# Total Balls = 291
# Run Rate = 5.67


run,over=map(float,input("enter run and overs").split())
overs=int(over)
current=int((over*10)%10)
balls=(overs*6)+current
rate= run/(overs+(current/6))
print(F"total balls ={balls}\nrun rate= ={rate}")