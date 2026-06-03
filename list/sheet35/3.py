# 3.

# =========================================================
#          MATRIX QUALITY CHECK SYSTEM
# =========================================================

# Scenario

# A manufacturing company records quality inspection values in
# matrix form. The Quality Control team wants a menu-driven
# application to analyze the inspection data and generate reports.

# The application should allow the user to:

# 1. Count Armstrong Numbers Row-wise
# 2. Count Palindrome Numbers Column-wise
# 3. Display Average of Each Row
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Count Armstrong Numbers Row-wise
#    2. Count Palindrome Numbers Column-wise
#    3. Display Average of Each Row
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Count Armstrong Numbers Row-wise
#    -------------------------------------------
#    Count and display the number of Armstrong numbers
#    present in each row.

#    Examples:
#    153, 370, 371, 407

# 5. Choice 2 - Count Palindrome Numbers Column-wise
#    -----------------------------------------------
#    Count and display the number of palindrome numbers
#    present in each column.

#    Examples:
#    121, 131, 444, 1221

# 6. Choice 3 - Display Average of Each Row
#    --------------------------------------
#    Calculate and display the average of each row.

# 7. Choice 4 - Exit
#    --------------------------------------
#    Display:
#    "Thank You for Using Matrix Quality Check System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Count Armstrong Numbers Row-wise
# 2. Count Palindrome Numbers Column-wise
# 3. Display Average of Each Row
# 4. Exit

# Enter your choice: 1

# Enter rows: 3
# Enter columns: 3

# Enter matrix elements:
# 153 121 10
# 370 22 44
# 407 15 131

# Output:
# Row 1 Armstrong Count = 1
# Row 2 Armstrong Count = 1
# Row 3 Armstrong Count = 1

# ---------------------------------------------------------

# Enter your choice: 2

# Output:
# Column 1 Palindrome Count = 0
# Column 2 Palindrome Count = 2
# Column 3 Palindrome Count = 2


print("""
=========================================================
            MATRIX QUALITY CHECK SYSTEM
=========================================================
""")

while True:
    print("""
Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit
          """)
    m=int(input("enter the option: "))

    match (m):
        case 1:
            r=int(input("enter the number of rows :"))
            c=int(input("enter the number of columns :"))

            mat1=[]

            for i in range(r):
                row=[]
                for j in range(c):
                    d=int(input("enter the value :"))
                    row.append(d)
                mat1.append(row)

            for i in range(r):
                count=0
                for j in range(c):
                    add=0
                    for k in str(mat1[i][j]):
                        add+=int(k)**3
                    if add==mat1[i][j]:
                        count+=1
                print("Row ",i,"amstrong count = ",count)
            
        case 2:
            r=int(input("enter the number of rows :"))
            c=int(input("enter the number of columns :"))

            mat1=[]

            for i in range(r):
                row=[]
                for j in range(c):
                    d=int(input("enter the value :"))
                    row.append(d)
                mat1.append(row)
            
            for j in range(c):
                count=0
                for i in range(r):
                    a=""
                    for k in str(mat1[i][j])[::-1]:
                        a=a+k
                    if str(mat1[i][j])==a:
                        count+=1
                print("Column ",i,"palindrome count = ",count)

        case 3:
            r=int(input("enter the number of rows :"))
            c=int(input("enter the number of columns :"))

            mat1=[]

            for i in range(r):
                row=[]
                for j in range(c):
                    d=int(input("enter the value :"))
                    row.append(d)
                mat1.append(row)
            
            for i in range(r):
                add=0
                for j in range(c):
                    add+=mat1[i][j]
                print("average number of row ",i," =",add/c)

        case 4:
            print("exit")
            break

