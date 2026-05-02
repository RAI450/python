# 10.Electricity Bill Processing System (Multi-House)
# An electricity board processes bills for multiple houses in a society.

# Write a program to:

# - Read number of houses n
# - For each house:
#     - Read units consumed
#     - Calculate bill using slab rates:

#         First 100 units      → ₹5 per unit  
#         Next 100 units      → ₹7 per unit  
#         Above 200 units     → ₹10 per unit  

#     - Apply conditions:
#         - If bill > ₹2000 → add 10% surcharge  
#         - If units < 50 → give ₹100 subsidy  

#     - Print bill for each house

# - After processing all houses:
#     - Print total bill collected
#     - Print highest bill

# ---

# Input:
# 3
# 120
# 250
# 40

# Output:
# House 1 Bill = 640
# House 2 Bill = 1700
# House 3 Bill = 100      # wrong it is 200

# Total Collection = 2440   #wrong it is 2540
# Highest Bill = 1700

n=int(input("enter number of houses"))

hig=""
total=0
a=0
for i in range(1,n+1):
    u=int(input("enter units for house"))
    if u<=100:
        bill=u*5
    elif u<=200:
        bill=(100*5)+((u-100)*7)
    else:
        bill=(100*5)+(100*7)+((u-200)*10)
    print("house ",i,"bill = ",bill)
    if bill>=a:
        a=bill
    total+=bill
    hig=hig+str(bill)

print("total collection = ",total)
print("highest bill = ",a)

    

