#while
# i = 1
# while i <= 6 and i<7:
#   print(i)
#   i += 1


# while with break
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     i += 1
#     continue


#while with continue
# i = 0
# while i < 6:
#     pass



# A function is a block of code which only runs when it is called.
#
# You can pass data, known as parameters, into a function.
#
# A function can return data as a result.
# def abc_xyz_123():
#   print("Hello from a function")
#
# abc_xyz_123()
#
# def my_function(a):
#     print(a + " Refsnes")
# my_function("123")
# my_function("234")
# my_function("356")

# def sum_compare(a,b):
#      sum=a+b
#      print(sum)
#      if a>b:
#          print("a is greater")
#      else:
#         print("b is greater")
#
# sum_compare(a=int(input()),b=int(input()))

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# A parameter is the variable listed inside the parentheses in the function definition.
#
# An argument is the value that is sent to the function when it is called

# def my_function(fname, lname):
#   print(fname + " " + lname)
# #
# my_function("Emil", "Refsnes")


# ********Arbitrary Arguments, *args
# arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function(play,two,*kids):
    print(kids)
    # for i in kids:
        # kids[3]='abc'
    print("The youngest child is " + kids[0])
#
my_function("Emil", "Tobias", "Linus","abc")



# Keyword Arguments
# You can also send arguments with the key = value syntax.
# def my_function( child2, child1,child3):
#   print("The youngest child is " ,child3)
#
# my_function(child1="Emil", child2="Tobias", child3="Linus")



# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments
# that will be passed into your function, add two asterisk:
# ** before the parameter name in the function definition.


# {
#     "fname":"1",
#     "lname":"2"
# }
# def my_function(**kid):
#   print(kid["fname"] + kid["lname"])
#
# my_function(fname = int(input("enter one number")), lname = int(input("enter one number")))




# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# def my_function(food):
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)

