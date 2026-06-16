# 5.Student Grade Classification System (Python List Assignment)
# A school stores student marks in a list. The system must analyze the marks and generate a *clear performance report* 
# by grouping students into grade categories.

# Write a Python program to:

# * Iterate through the list of marks
# * Assign grades based on marks:

#   * *>= 90 → A*
#   * *>= 75 and < 90 → B*
#   * *>= 50 and < 75 → C*
#   * *< 50 → Fail*
# * Store each category in separate lists
# * Count students in each category
# * Display a *final structured report (important)*

# ---

# ## 📌 Output Format (Mandatory)

# Your output must be displayed exactly in this format:


# ===== STUDENT GRADE REPORT =====

# A Grade Students   : [list]
# B Grade Students   : [list]
# C Grade Students   : [list]
# Fail Students      : [list]

# --------------------------------
# A Count   : X
# B Count   : X
# C Count   : X
# Fail Count: X
# --------------------------------

# Total Students: X


# ---

#  Input

# [95, 82, 67, 45, 30]

# Output


# ===== STUDENT GRADE REPORT =====

# A Grade Students   : [95]
# B Grade Students   : [82]
# C Grade Students   : [67]
# Fail Students      : [45, 30]

# --------------------------------
# A Count   : 1
# B Count   : 1
# C Count   : 1
# Fail Count: 2
# --------------------------------

# Total Students: 5

m=int(input("enter the number of integers "))
n=[]
a=[]
b=[]
c=[]
fail=[]
for i in range(m):
    s=int(input("enter the integers "+str(i+1)+": "))
    if s>=90:
        a.append(s)
    elif s>=75:
        b.append(s)
    elif s>=50:
        c.append(s)
    else:
        fail.append(s)

print("===== STUDENT GRADE REPORT =====")
print()
print("A Grade Students   :",a)
print("B Grade Students   :",b)
print("C Grade Students   :",c)
print("Fail  Students     :",fail)
print()

print("--------------------------------")
print("A count     : ",len(a))
print("B count     : ",len(b))
print("C count     : ",len(c))
print("Fail count  : ",len(fail))
print("--------------------------------")

print("total students: ",m)