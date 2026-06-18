# 3.
# ONLINE SHOPPING SYSTEM

# Scenario:

# An e-commerce company wants to develop an Online Shopping System. The application should be menu-driven and should demonstrate different types of arguments used in Python functions.


# Requirements

# Choice 1 – Customer Registration

# * Accept Customer Name, Email, and Mobile Number.
# * Pass the values to a function using Positional Arguments.
# * Display the registered customer details.

# Choice 2 – Product Information

# * Accept Product Name, Price, and Category.
# * Call the function using Keyword Arguments.
# * Display the product details.

# Choice 3 – Generate Invoice

# * Accept Product Name and Price.
# * Tax Percentage should have a default value.
# * Use Default Arguments while generating the invoice.
# * Display the final amount.

# Choice 4 – Add Multiple Products

# * Allow the user to enter any number of product prices.
# * Pass all prices to a function using Variable Length Arguments (*args).
# * Calculate and display the total bill amount.

# Choice 5 – Display Customer Profile

# * Accept any number of customer details such as Name, City, Email, Mobile, Membership Type, etc.
# * Pass the details using Arbitrary Keyword Arguments (**kwargs).
# * Display all customer information.

# Choice 6 – Exit

# Sample Execution

# Enter Choice : 1

# Enter Name : Ajay
# Enter Email : [ajay@gmail.com](mailto:ajay@gmail.com)
# Enter Mobile : 9876543210

# Customer Registered Successfully

# ---

# Enter Choice : 2

# Enter Product Name : Laptop
# Enter Price : 55000
# Enter Category : Electronics

# Product Details Displayed Successfully

# ---

# Enter Choice : 3

# Enter Product Name : Laptop
# Enter Price : 55000

# Invoice Generated Successfully

# ---

# Enter Choice : 4

# Enter Number of Products : 4

# Enter Price 1 : 100
# Enter Price 2 : 200
# Enter Price 3 : 300
# Enter Price 4 : 400

# Total Bill Amount : 1000

# ---

# Enter Choice : 5

# Customer Profile Displayed Successfully

# ---

# Enter Choice : 6

# Thank You. Program Terminated.

# Important Instructions

# 1. Choice 1 must use Positional Arguments.
# 2. Choice 2 must use Keyword Arguments.
# 3. Choice 3 must use Default Arguments.
# 4. Choice 4 must use Variable Length Arguments (*args).
# 5. Choice 5 must use Arbitrary Keyword Arguments (**kwargs).
# 6. Use separate functions for each menu option.
# 7. Implement the solution using a menu-driven approach.
# 8. Maintain proper code readability and formatting.

# Note:
# Marks will be awarded based on the correct usage of the specified argument type in each menu option.
def dtl(a,b,c):
    print("name = ",a)
    print("email = ",b)
    print("mobile number = ",c)
def pro(name,price,category):
    print(name)
    print(price)
    print(category)

def add(*t):
    total=0
    for i in t:
        total+=i
    return total

def display(**kwargs):
    print(kwargs)
while True:
    print("""
    1. Customer Registration
    2. Product Information
    3. Generate Invoice
    4. Add Multiple Products
    5. Display Customer Profile
    6. Exit
        """)
    n=int(input("enter the choice: "))
    match n:
        case 1:
            s=input("enter the name: ")
            em=input("enter the mail: ")
            m=int(input("enter the mobile number: "))
            dtl(s,em,m)
            print("Customer Registered Successfully")

        case 2:
            s=input("enter the product name: ")
            p=int(input("enter the product price: "))
            c=input("enter the category: ")
            pro(name=s,price=p,category=c)
            print("Product Details Displayed Successfully")
        
        case 3:
            print("not done")
        
        case 4:
            t=[]
            s=int(input("enter the number of products: "))
            for i in range(s):
                p=int(input("enter the price: "))
                t.append(p)
            print("total bill amount: ",add(*t))
        
        case 5:
            s=input("enter the product name: ")
            p=int(input("enter the product price: "))
            c=input("enter the category: ")
            display(name=s,price=p,category=c)
        case 6:
            print("Thank You. Program Terminated.")
            break
        
        case _:
            print("invalid input")

