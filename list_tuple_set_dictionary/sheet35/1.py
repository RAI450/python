# 1.
# =========================================================
#         MATRIX OPERATIONS MANAGEMENT SYSTEM
# =========================================================


# A data analysis company stores numerical information in matrix form.
# To help employees perform matrix-related operations efficiently,
# the company wants a menu-driven application.

# The application should allow the user to:

# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# The user must enter the number of rows, columns, and all matrix
# elements. The program should perform the selected operation and
# display the result.

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user chooses Exit.

#    1. Add Two Matrices
#    2. Subtract Two Matrices
#    3. Compare Two Matrices
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all elements of Matrix A and Matrix B from the user whenever
#    required.

# 4. Based on the user's choice:

#    Choice 1 - Add Two Matrices
#    --------------------------------
#    Add corresponding elements of both matrices and display
#    the resultant matrix.

# 5. Choice 2 - Subtract Two Matrices
#    --------------------------------
#    Subtract corresponding elements of Matrix B from Matrix A
#    and display the resultant matrix.

# 6. Choice 3 - Compare Two Matrices
#    --------------------------------
#    Check whether both matrices are equal.

#    Two matrices are considered equal if:
#    - They have the same dimensions.
#    - Corresponding elements are equal.

#    Display:
#    "Matrices are Equal"
#    or
#    "Matrices are Not Equal"

# 7. Choice 4 - Exit
#    --------------------------------
#    Display:
#    "Thank You for Using Matrix Operations Management System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 1

# Enter number of rows: 2
# Enter number of columns: 2

# Enter Matrix A:
# 1 2
# 3 4

# Enter Matrix B:
# 5 6
# 7 8

# Result Matrix:
# 6 8
# 10 12

# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 3

# Enter number of rows: 2
# Enter number of columns: 2

# Enter Matrix A:
# 1 2
# 3 4

# Enter Matrix B:
# 1 2
# 3 4

# Output:
# Matrices are Equal

# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 4

# Output:
# Thank You for Using Matrix Operations Management System
    


print("""
=======================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=======================================================
""")

while True:
    print("""
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit
          """)
    m=int(input("enter the option: "))

    match (m):

        case 1:
            print("Adding matrices")

            r=int(input("enter the number of rows :"))
            c=int(input("enter the number of columns :"))

            mat1=[]

            for i in range(r):
                row=[]
                for j in range(c):
                    d=int(input("enter the value :"))
                    row.append(d)
                mat1.append(row)

            r2=int(input("enter the number of rows :"))
            c2=int(input("enter the number of columns :"))

            mat2=[]

            for i in range(r2):
                row=[]
                for j in range(c2):
                    d=int(input("enter the value :"))
                    row.append(d)
                mat2.append(row)
            
            if r==r2 and c==c2:
                res=[]
                for i in range(r):
                    row=[]
                    for j in range(c):
                        l=mat1[i][j]+mat2[i][j]
                        row.append(l)
                    res.append(row)
                print("resulting matrix ---",res)
            else:
                print("both matrix length should be same")

        case 2:
            print("Subtracting matrices")

            r=int(input("enter the number of rows :"))
            c=int(input("enter the number of columns :"))

            mat1=[]

            for i in range(r):
                row=[]
                for j in range(c):
                    d=int(input("enter the value :"))
                    row.append(d)
                mat1.append(row)

            r2=int(input("enter the number of rows :"))
            c2=int(input("enter the number of columns :"))

            mat2=[]

            for i in range(r2):
                row=[]
                for j in range(c2):
                    d=int(input("enter the value :"))
                    row.append(d)
                mat2.append(row)
            
            if r==r2 and c==c2:
                res=[]
                for i in range(r):
                    row=[]
                    for j in range(c):
                        l=mat1[i][j]-mat2[i][j]
                        row.append(l)
                    res.append(row)
                print("resultant matrix ---",res)
            else:
                print("both matrix length should be same")
        case 3:
            print("Comparing matrices")

            r=int(input("enter the number of rows :"))
            c=int(input("enter the number of columns :"))

            mat1=[]

            for i in range(r):
                row=[]
                for j in range(c):
                    d=int(input("enter the value :"))
                    row.append(d)
                mat1.append(row)

            r2=int(input("enter the number of rows :"))
            c2=int(input("enter the number of columns :"))

            mat2=[]

            for i in range(r2):
                row=[]
                for j in range(c2):
                    d=int(input("enter the value :"))
                    row.append(d)
                mat2.append(row)
            
            if r==r2 and c==c2:
                flag=1
                for i in range(r):
                    for j in range(c):
                        if mat1[i][j]!=mat2[i][j]:
                            flag=0
                            break
                    if flag==0:
                        print("matrices are not equal")
                        break
                else:
                    print("matrices are equal")


            else:
                print("matrix are not equal")

        case 4:
            print("Thank You for Using Matrix Operations Management System")
            break