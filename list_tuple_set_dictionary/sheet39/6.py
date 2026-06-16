# 6.

# =========================================
# MOBILE APP DOWNLOAD COUNTER
# ===========================

# Downloads received from different cities:

# cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

# Write a program to:

# * Count downloads city-wise.
# * Display city with maximum downloads.

# Sample Output:
# {'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
# Most Downloads : Indore

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

c={}
for x in cities:
    c[x]=c.get(x,0)+1
print(c)

max=0
high=""
for k,v in c.items():
    if v>max:
        max=v
        high=k
print("most downloads : ",high)
    