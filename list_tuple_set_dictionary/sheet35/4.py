# 4.

# =========================================================
#         MATRIX DIAGONAL ANALYSIS SYSTEM
# =========================================================

# Scenario

# A security company stores surveillance data in matrix form.
# The analyst wants a menu-driven application to examine the
# diagonal elements of the matrix and generate reports.

# The application should allow the user to:

# 1. Display Main Diagonal Elements
# 2. Display Secondary Diagonal Elements
# 3. Compare Main and Secondary Diagonal Sums
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Display Main Diagonal Elements
#    2. Display Secondary Diagonal Elements
#    3. Compare Main and Secondary Diagonal Sums
#    4. Exit

# 2. Read the size of a square matrix from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Display Main Diagonal Elements
#    -----------------------------------------
#    Display all elements present in the main diagonal.

# 5. Choice 2 - Display Secondary Diagonal Elements
#    ----------------------------------------------
#    Display all elements present in the secondary diagonal.

# 6. Choice 3 - Compare Main and Secondary Diagonal Sums
#    ---------------------------------------------------
#    Calculate the sum of both diagonals and display:

#    - Main Diagonal Sum
#    - Secondary Diagonal Sum
#    - Which diagonal has the greater sum
#    - Or whether both sums are equal

# 7. Choice 4 - Exit
#    -----------------------------------------
#    Display:
#    "Thank You for Using Matrix Diagonal Analysis System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Enter size of matrix: 3

# Enter matrix elements:

# 1 2 3
# 4 5 6
# 7 8 9

# Menu
# 1. Display Main Diagonal Elements
# 2. Display Secondary Diagonal Elements
# 3. Compare Main and Secondary Diagonal Sums
# 4. Exit

# Enter your choice: 1

# Output:
# Main Diagonal Elements:
# 1 5 9

# ---------------------------------------------------------

# Enter your choice: 2

# Output:
# Secondary Diagonal Elements:
# 3 5 7

# ---------------------------------------------------------

# Enter your choice: 3

# Output:
# Main Diagonal Sum = 15
# Secondary Diagonal Sum = 15
# Both Diagonal Sums are Equal


print("""
=========================================================
            MATRIX DIAGONAL CHECK SYSTEM
=========================================================
""")

while True:
    print("""
Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
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
            
            a=""
            for i in range(r):
                for j in range(c):
                    if i==j:
                        a+=str(mat1[i][j])+" "
            print("main diagonal elements :",a)
        
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

            b=""
            a=c-1
            for i in range(r):
                for j in range(c):
                    if j==a:
                        b+=str(mat1[i][j])+" "
                        a-=1
            print("secondary diagonal elements :",b)

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
            
            b=""
            a=c-1
            sum1=0
            sum2=0
            for i in range(r):
                for j in range(c):
                    if j==a:
                        sum1+=mat1[i][j]
                        a-=1
            a=""
            for i in range(r):
                for j in range(c):
                    if i==j:
                        sum2+=mat1[i][j]
            
            if sum1==sum2:
                print("both sums are equal")
            else:
                print("both sums are not equal")

        case 4:
            print("exit")
            break