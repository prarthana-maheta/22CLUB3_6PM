# # #  Write a Python program to create a dictionary from a string.
# # # Note: Track the count of the letters from the string.
# # # Sample string : 'w3resource'
# # # Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# #
# #
# # # Write a Python program to match key values in two dictionaries.
# # # Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# # # Expected output: key1: 1 is present in both x and y
# #
# #
# #
# # # Array:
# # # Python does not have built-in support for Arrays, but Python Lists can be used instead.
# # #
# # # arr1=[1,2,3]
# # #
# # # x = len(arr1)
# #
# # # append()	Adds an element at the end of the list
# # # clear()	Removes all the elements from the list
# # # copy()	Returns a copy of the list
# # # count()	Returns the number of elements with the specified value
# # # extend()	Add the elements of a list (or any iterable), to the end of the current list
# # # index()	Returns the index of the first element with the specified value
# # # insert()	Adds an element at the specified position
# # # pop()	Removes the element at the specified position
# # # remove()	Removes the first item with the specified value
# # # reverse()	Reverses the order of the list
# # # sort()	Sorts the list
# #
# #
# # # Python Classes/Objects
# # # Python is an object oriented programming language.
# # #
# # # Almost everything in Python is an object, with its properties and methods.
# # #
# # # A Class is like an object constructor, or a "blueprint" for creating objects.
# #
# # # x=3
# class MyClass:
#
#       x=5
#       def display(self,x):
#         self.x=2
#         print(x)
#         print(self.x)
#
#   # def calling(self):
#   #   print(x)
#   #   print(self.x)
#
# a=MyClass()
# a.display(2)
# # print(x)
# #
# # # creating objects:
# # # p1 = MyClass()
# # # print(p1.x)
# # #
# # The __init__() Function
# # The examples above are classes and objects in their simplest form,
# # and are not really useful in real life applications.
# #
# # To understand the meaning of classes we have to understand
# # the built-in __init__() function.
# #
# # All classes have a function called __init__(),
# # which is always executed when the class is being initiated.
# #
# # Use the __init__() function to assign values to object properties,
# # or other operations that are necessary to do when the object is being created:

#
# # The self Parameter
# # The self parameter is a reference to the current instance of the class,
# # and is used to access variables that belongs to the class.
#
class Person:

  def __init__(self, name,height, age):
    print("init")
    self.name = name
    self.age = age
    self.height=100

  def myfunc(self,height):
    # print("Hello my name is " )
    # print(self.name)
    print(self.height)
  #
  #   if 100 >= height:
  #     print("height is low")

p1 = Person('ankit','6 foot',50)
p1.myfunc(78)


#
#
#
# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age
# #
# # p1 = Person("John", 36)
# #
# # print(p1.name)
# # print(p1.age)
#
# #
# # __call__ in Python
# # Python has a set of built-in methods and __call__ is one of them.
# # The __call__ method enables Python programmers to write classes where the instances
# # behave like functions and can be called like a function. When the instance is called
# # as a function; if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).
#
#
# # class Example:
# #     def __init__(self):
# #         print("Instance Created")
# #
# #     # Defining __call__ method
# #     def __call__(self):
# #         print("Instance is called via special method")
# #
# #
# # # Instance created
# # e = Example()
# #
# # # __call__ method will be called
# # e()
#
#
# # class Product:
# #     def __init__(self):
# #         print("Instance Created")
# #
# #     # Defining __call__ method
# #     def __call__(self, a, b):
# #         print(a * b)
# #
# #
# # # Instance created
# # ans = Product()
# #
# # # __call__ method will be called
# # ans(10, 20)
#
#
# # The __str__() Function
# # The __str__() function controls what should be returned when the class object is represented as a string.
#
# # The string representation of an object WITHOUT the __str__() function:
# #
# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age
# #
# # p1 = Person("John", 36)
# #
# # print(p1)
#
# # The string representation of an object WITH the __str__() function:
# #
# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age
# #
# #   def __str__(self):
# #     return f"{self.name}({self.age})"
# #
# # p1 = Person("John", 36)
# #
# # print(p1)

# class MyClass:
#     x = 5
#     sum = 0
#     def sum_num(self,x):
#         self.sum=self.x+x
#     def display(self):
#         print('sum = ',self.sum)
#
# a = MyClass
# # a.Sum(5)
# # a.display()
# a.sum_num(5)