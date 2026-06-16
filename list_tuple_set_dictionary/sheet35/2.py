# 2.
# =========================================================
#             MATRIX ANALYSIS SYSTEM
# =========================================================


# A research laboratory stores experimental data in matrix form.
# Scientists want a program that can analyze the matrix and provide
# different statistics through a menu-driven application.

# The application should allow the user to:

# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Count Prime Numbers Row-wise
#    2. Count Perfect Numbers Column-wise
#    3. Display Row-wise Sum
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Count Prime Numbers Row-wise
#    ---------------------------------------
#    Count and display the number of prime numbers present
#    in each row of the matrix.

# 5. Choice 2 - Count Perfect Numbers Column-wise
#    --------------------------------------------
#    Count and display the number of perfect numbers present
#    in each column of the matrix.

#    Note:
#    A perfect number is a number that is equal to the sum
#    of its proper divisors.

#    Examples:
#    6  = 1 + 2 + 3
#    28 = 1 + 2 + 4 + 7 + 14

# 6. Choice 3 - Display Row-wise Sum
#    --------------------------------
#    Calculate and display the sum of each row.

# 7. Choice 4 - Exit
#    --------------------------------
#    Display:
#    "Thank You for Using Matrix Analysis System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 1

# Enter rows: 3
# Enter columns: 3

# Enter matrix elements:
# 2 4 5
# 6 7 8
# 11 28 13

# Output:
# Row 1 Prime Count = 2
# Row 2 Prime Count = 1
# Row 3 Prime Count = 2

# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 2

# Output:
# Column 1 Perfect Number Count = 1
# Column 2 Perfect Number Count = 1
# Column 3 Perfect Number Count = 0

# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 3

# Output:
# Row 1 Sum = 11
# Row 2 Sum = 21
# Row 3 Sum = 52

# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 4

# Output:
# Thank You for Using Matrix Analysis System


print("""
=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================
""")

while True:
    print("""
Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
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
                    if mat1[i][j]==2 or mat1[i][j]==3:
                        count+=1
                    elif mat1[i][j]<2:
                        count+=0
                    else:
                        for k in range(2,(mat1[i][j]//2)+1):
                            if mat1[i][j]%k==0:
                                break
                        else:
                            count+=1
                print("Row ",i," = ",count)

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
                    sum=0
                    if mat1[i][j]<2:
                        count+=0
                    else:
                        for k in range(1,(mat1[i][j]//2)+1):
                            if mat1[i][j]%k==0:
                                sum=sum+k
                        if sum==mat1[i][j]:
                            count+=1
                print("column ",j," = ",count)
            
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
                print("Row ",i," = ",add)
                
        case 4:
            print("thankyou for using matrix analysis system")
            break






