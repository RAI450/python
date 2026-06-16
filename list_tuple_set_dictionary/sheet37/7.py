# 7. A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

# Tuple Format:

# (player_id, player_name, runs_scored)

# Requirements:

# Read N player records from the user and store them as tuples in a list.
# Display all player records.
# Find and display the player who scored the highest runs.
# Find and display the player who scored the lowest runs.
# Calculate and display the total runs scored by all players.
# Calculate and display the average runs scored.
# Display players who scored more than 50 runs.

# Test Case:

# Input:

# Enter number of players: 5

# 101 Virat 82
# 102 Rohit 45
# 103 Gill 120
# 104 Hardik 38
# 105 SKY 76

# Expected Output:

# All Players:
# (101, 'Virat', 82)
# (102, 'Rohit', 45)
# (103, 'Gill', 120)
# (104, 'Hardik', 38)
# (105, 'SKY', 76)

# Highest Scorer:
# (103, 'Gill', 120)

# Lowest Scorer:
# (104, 'Hardik', 38)

# Total Runs:
# 361

# Average Runs:
# 72.2

# Players Scoring More Than 50 Runs:
# (101, 'Virat', 82)
# (103, 'Gill', 120)
# (105, 'SKY', 76)

n=int(input("enter the number of plyers"))

rec=[]
for i in range(1,n+1):
    id=int(input("enter the id: "))
    name=input("enter the name: ")
    run=int(input("enter the runs: "))
    s=(id,name,run)
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
    if i[2]>50:
        hc.append(i)

print("highest scorer: ",bda)
print("lowest scorer: ",chota)
print("total runs: ",add)
print("average runs: ",add/n)

for i in hc:
    print(i)
    
