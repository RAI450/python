# 3.MATRIX PERFORMANCE EVALUATION SYSTEM

# A company records the monthly performance scores of employees in a matrix format. 
# Each row represents an employee and each column represents a month.
# The HR department wants a menu-driven application to analyze employee performance.

# Menu
# 1. Find Employee with Highest Total Score
# 2. Find Month with Lowest Average Score
# 3. Display Employee-wise Maximum Score
# 4. Exit
# Requirements
# Choice 1 – Find Employee with Highest Total Score
# Calculate the sum of each row.
# Display the employee number having the highest total score.
# Choice 2 – Find Month with Lowest Average Score
# Calculate the average of each column.
# Display the month having the lowest average score.
# Choice 3 – Display Employee-wise Maximum Score
# Find and display the maximum value present in each row.
# Sample Input
# 10 20 30
# 40 50 60
# 25 35 45

# Output
# Employee 2 has Highest Total Score = 150

# Month 1 Average = 25
# Month 2 Average = 35
# Month 3 Average = 45

# Employee 1 Max Score = 30
# Employee 2 Max Score = 60
# Employee 3 Max Score = 45

r=int(input("enter number of employees :"))
c=int(input("enter number of months :"))

mat=[]
for i in range(r):
    row=[]
    for j in range(c):
        d=int(input("enter the score for employee "+str(i+1)+" for month "+str(j+1)+" :"))
        row.append(d)
    mat.append(row)

for i in mat:
    print(i)

while True:
    print("""
    Menu
    1. Find Employee with Highest Total Score
    2. Find Month with Lowest Average Score
    3. Display Employee-wise Maximum Score
    4. Exit
        """)
    m=int(input("choose option : "))

    match m:
        case 1:
            add=0
            ind=0
            for i in range(len(mat)):
                adi=0
                for j in mat[i]:
                    adi+=j
                if adi>add:
                    add=adi
                    ind=i+1
            print("Employee ",ind," has Highest Total Score = ",add)
        case 2:
            for j in range(c):
                add=0
                for i in range(r):
                    add+=mat[i][j]
                print("Month ",j+1," Average = ",add/c)
        case 3:
            for i in range(r):
                max=0
                for j in range(c):
                    if mat[i][j]>max:
                        max=mat[i][j]
                print("Employee ",i+1," Max Score = ",max)

        case 4:
            print("exit")
            break



