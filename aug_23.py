# # # The return Statement
# # # The statement return [expression] exits a function,
# # # optionally passing back an expression to the caller.
# # # A return statement with no arguments is the same as return None.
# #
# # # Function definition is here
# #
# # # def my_function(**kid):
# # #   print(kid["fname"] + kid["lname"])
# # #
# # # my_function(fname = int(input("enter one number")), lname = int(input("enter one number")))
# #
# #

# def sum( arg1, arg2 ):
#    # Add both the parameters and return them."
#    total = arg1 + arg2
#    print("Inside the function : ", total)
#    return total
# print("hrllo")
#
# def sub(arg1):
#     print(arg1-10)
#
# # Now you can call sum function
# total = sum( 10, 20 )
# sub(total)
# print("Outside the function : ", total)
#
# # output:
# # prarthana kamleshbhai maheta
#
def print_name(m,f,l):
    return f"my full name is: {f} {m} {l}"
a=print_name(f="A",m="B",l="C")
print(a)
#
# # Default arguments
#
# # # Function definition is here
def printinfo( name, age=0):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age ", age)
   return

# # # Now you can call printinfo function
# # printinfo( name="miki" )
# # print(a)
# # printinfo( name="miki" )
#
# #
# # Variable-length arguments
# # You may need to process a function for more arguments than you specified
# # while defining the function. These arguments are called variable-length arguments
# # and are not named in the function definition, unlike required and default arguments.
#
# # Function definition is here
# # a=1
# # a=2
# # a={"a":2}
# # print(a)
# def printinfo( **arg1):
#    "This prints a variable passed arguments"
#    # (60,50)
#    # print(args1[0])
#    print(arg1['fname'])
# #
# #    def print_name(arg1):
# #       print("Output is:",arg1)
# #       return
# #    print_name(arg1)
# #
# # # Now you can call printinfo function
# printinfo( 10,20,40,80,fname=2 )
# # printinfo( 70, 60, 50 )
#
#
#
# # Lambda function
# # A lambda function is a small anonymous function.
# #
# # A lambda function can take any number of arguments, but can only have one expression.
#
# # Why Use Lambda Functions?
# # The power of lambda is better shown when you use them as an anonymous function inside another function.
#
# # lambda arguments : expression
b=1
# def sum(a,**b):
#     print(a + 10)
#     return
# print(sum(5,b))
# #
# x = lambda a: a + 10  if a>1 else None
# print(x(5))

# a=["hello"]
# print(a*5)
#
# a=1
# x = lambda a, *b,**d: print(d)
# print(x(5,6,7,c=1))

pets = ['cats', 'dogs', 'fishes', 'rabbits', 'hamsters', 'parrots', 'ferrets']
l1=[]
# for word in pets[::-1]:
#     l1.append(word)
    # print(word)
print(pets)
pets.reverse()
print(pets)

print(list(reversed(pets)))

# l1.sort(reverse=True)
# print(l1)
# #
# # # pets=['a','c','d','b']
# # pets = ['cats', 'dogs', 'fishes', 'rabbits', 'hamsters', 'parrots', 'ferrets']
# # pets.sort(key=lambda word: word[::-1])
# # print(pets)
#
#
#
#
# product = (lambda *a: a**2)
# print("The product is:", product(10, 20))
#
# text = (lambda x="Java", y = " is", z = " my favourite": x + y + z)
# print(text("Python"))
#
#
#
# #
# # Scope of Variables
# # All variables in a program may not be accessible at all locations in that program.
# # This depends on where you have declared a variable.
# #
# # The scope of a variable determines the portion of the program where you can access a particular identifier.
# # There are two basic scopes of variables in Python −
# #
# # Global variables
# # Local variables
#
#
total = 0 # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   # glal total
   total = arg1 + arg2 # Here total is local variable.
   print("Inside the function local total : ", total)
   return total
print(total)
# Now you can call sum function
sum( 10, 20 )
print("Outside the function global total : ", total)
#
# def func_1(x1):
#     # func_2()
#     x=lambda x: x * x if x == 1 else x + 1
#     return x(x1)

# print(func_1(1))
# print(x1)

#
# def func_2(x):
#     x*x
#
# func_1(1)
# # lambda x : x*x if x==1 else x*1
# # print(key(2))
# #
# # # 1
# # Write a Python program to find whether a given year is a leap year or not.
# #
# # Test Data : 2016
# #
# # Expected Output :
# # 2016 is a leap year.
#
# # 2
# # Write a Python program to find the largest of three numbers.
# # Test Data : 12 25 52
# # Expected Execution:
# # 1st Number = 52
# # 2nd Number = 25
# # 3rd Number = 12
#
# #3
# # Take values of length and breadth of a rectangle from user and check if it is square or not.
#
# #4
# # Take values of length  of a square from user and find area of a square.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #######################1#######################
# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
#
# year = int(input("Enter a year: "))
#
# if is_leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
#
#
#
# ##############################2########################
# # def find_largest_number(a, b, c):
# #     if a >= b and a >= c:
# #         return a
# #     elif b >= a and b >= c:
# #         return b
# #     else:
# #         return c
# #
# # # Input three numbers
# # num1 = float(input("Enter the 1st number: "))
# # num2 = float(input("Enter the 2nd number: "))
# # num3 = float(input("Enter the 3rd number: "))
# #
# # largest_number = find_largest_number(num1, num2, num3)
# #
# # print("1st Number =", num1)
# # print("2nd Number =", num2)
# # print("3rd Number =", num3)
# # print(f"The largest number is {largest_number}")
#
#
# ################3##########################
#
# length = float(input("Enter the length of the rectangle: "))
# breadth = float(input("Enter the breadth of the rectangle: "))
#
# if length == breadth:
#     print("It is a square.")
# else:
#     print("It is not a square.")
#
#
# #########################4####################
# def calculate_square_area(side_length):
#     area = side_length ** 2
#     return area
#
# # Input the length of the square's side from the user
# side_length = float(input("Enter the length of the square's side: "))
#
# # Calculate the area of the square
# area = calculate_square_area(side_length)
#
# print(f"The area of the square with side length {side_length} is {area}")


# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))
# num3 = float(input("Enter the 3rd number: "))
# #
l1=lambda num1,num2,num3: print("a is first",num1) if num1>=num2 and num1>=num3 else None

# if num1<num2 or num3<num2:
#     print("b is second",num2)
# elif num1<num3

l3=lambda num2,num3:print("c is second",num3) if num3<=num2 else print("b is second",num2)
max1=l1(num1,num2,num3)
max3=l3(num2,num3)
print(max1)
# l2=lambda

# def m2m(a,b,c):
#     if a>=b and a>=c:
#         print("a is first")
#
# m2m(4,5,6)

# l1=[num1,num2,num3]
# max1