# 6. Weather Monitoring System
#    A system checks weather conditions:

# * If temperature ≥ 30 → Hot day
# * If humidity ≥ 70 → High humidity alert

# Input:
# Enter temperature: 32
# Enter humidity: 75

# Output:
# Hot day
# High humidity alert
temp=int(input("enter temperature :"))
hum=int(input("enter humidity :"))
if temp>=30:
    print("hot day")
    if hum>=75:
        print("high humidity alert ")