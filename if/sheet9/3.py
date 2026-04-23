# 3. Smart Scholarship Allocation System

# A scholarship is provided based on marks, family income, and category.

# If marks are 85 or above, then check income. If income is less than or equal to 300000, then check category.
# If category is not general, give Full Scholarship; otherwise give 75% Scholarship.
# If income is above 300000, give 50% Scholarship.

# If marks are between 70 and 84, then check income.
# If income is less than or equal to 200000, give 50% Scholarship; otherwise give 25% Scholarship.

# If marks are below 70, no scholarship is given.

# Input:
# Marks = 88
# Income = 250000
# Category = OBC

# Output:
# Scholarship = Full Scholarship

mrk=int(input("enter  marks "))
inc=int(input("enter income "))
cat=input("enter category ")

if mrk>=85:
    if inc<=300000:
        if cat!="general":
            print("full scholarship granted")
        else:
            print("75% scholarship granted")
    else:
        print("50% scholarship granted")
elif mrk>=70:
    if inc<=200000:
        print("50% scholarship granted")
    else:
        print("25% scholarship granted")
else:
    print("no scholarship granted")

