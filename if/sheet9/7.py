# 7. University Result Classification System

# A university assigns final class based on marks, backlog, and project score.

# If marks are 75 or above, then check backlog. If backlog is 0, then check project score.
# If project score is 80 or above, assign First Class with Distinction; otherwise First Class.
# If backlog is not 0, assign First Class.

# If marks are between 60 and 74, then check backlog. 
# If backlog is less than or equal to 2, assign Second Class; otherwise Pass Class.

# If marks are between 50 and 59, assign Pass. Otherwise Fail.

# Input:
# Marks = 78
# Backlogs = 0
# Project = 85

# Output:
# Result = First Class with Distinction

mrk=int(input("enter marks "))
bklog=int(input("enter backlogs "))
proj=int(input("enter project "))

if mrk>=75:
    if bklog==0:
        if proj>=80:
            print("first class with distinction")
        else:
            print("first class")
    else:
        print("first class")
elif mrk>=60:
    if bklog<=2:
        print("second class")
    else:
        print("pass")
elif mrk>=50:
    print("pass")
else:
    print("fail")
