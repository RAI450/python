# 5. Smart Exam Evaluation System

# A student’s result depends on marks, attendance, and internal score.

# If marks are 40 or above, then check attendance. If attendance is 75 or above, then check internal marks. 
# If internal is 20 or above, result is Pass; otherwise Grace Pass. If attendance is below 75, result is Detained.

# If marks are below 40, then check if marks are at least 35 and internal is at least 25. If yes, result is Reappear; otherwise Fail.

# Input:
# Marks = 38
# Attendance = 80
# Internal = 26

# Output:
# Result = Reappear

mrk=int(input("enter marks "))
atten=int(input("enter attendance "))
itnl=int(input("enter internal score "))

if mrk>=40:
    if atten>=75:
        if itnl>=20:
            print("result = pass")
        else:
            print("result = grace pass")
    else:
        print("result = detained")
elif mrk>=35 and itnl>=25:
    print("result = reappear")
else:
    print("fail")

