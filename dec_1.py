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
#     x=5
#     def display(self,x):
#         self.x = 2
#         # print(x)
#         print(self.x)
#     # print(x)
#     def calling(self):
#         self.display(7)
#         self.x=10
#         print(self.x)
#
# a=MyClass()
# a.display(3)
# a.calling()
# a.display(3)
# print(x)
# #
# # # creating objects:
# # # p1 = MyClass()
# # # print(p1.x)
# # #
# # The __init__() Function
# # The examples above are classes and objects in their simplest form,
# # and are not really useful in real life applications.
# # #
# # # To understand the meaning of classes we have to understand
# # # the built-in __init__() function.
# # #
# # # All classes have a function called __init__(),
# # # which is always executed when the class is being initiated.
# # #
# # # Use the __init__() function to assign values to object properties,
# # # or other operations that are necessary to do when the object is being created:
#
# #
# # # The self Parameter
# # # The self parameter is a reference to the current instance of the class,
# # # and is used to access variables that belongs to the class.
# #
# # # def fun1()
# class Person:
#   def __init__(self, name,height, **age):
#     print("init")
#     self.name = name
#     self.age = age
#     self.height=100
#     print(age)
#
#   def myfunc(self,height):
#     # print("Hello my name is " )
#     print(self.name)
#     print(self.height)
#     if 100 >= height:
#       print("height is low")
#
# p1 = Person('ankit','6 ',dob=5101999)
# p2 = Person('ankit',6,dob=5101999)
# p1.myfunc(78)
# p2.myfunc()

# #
# #
# # #
# # #
# # #
# # # # class Person:
# # # #   def __init__(self, name, age):
# # # #     self.name = name
# # # #     self.age = age
# # # #
# # # # p1 = Person("John", 36)
# # # #
# # # # print(p1.name)
# # # # print(p1.age)
# # #
# # # #
# # # # __call__ in Python
# # # # Python has a set of built-in methods and __call__ is one of them.
# # # # The __call__ method enables Python programmers to write classes where the instances
# # # # behave like functions and can be called like a function. When the instance is called
# # # # as a function; if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).
# # #
# # #
# class Example:
#     def __init__(self):
#         print("Instance Created")
#     # def display(self):
#     #   print("Instance is called via special method")
#     # Defining __call__ method
#     def __call__(self,a):
#         print("Instance is called via special method",a)
# # # Instance created
# e = Example()
# e.__init__()
# __call__ method will be called__call__
# e("123")

# #
# # #
# # #
# # class Product:
# #     def __init__(self):
# #         print("Instance Created")
# #
# #     # Defining __call__ method
# #     def __call__(self, a, b):
# #         print(a * b)
# #     def mutiply(self,a,b):
# #         print(a/b)
# #
# # # Instance created
# # ans = Product()
# #
# # # __call__ method will be called
# # ans(10, 20)
# # ans.mutiply(10,20)
# # #
# # #
# # # # The __str__() Function
# # # # The __str__() function controls what should be returned when the class object is represented as a string.
# # #
# # # # The string representation of an object WITHOUT the __str__() function:
# # # #
# class Person:
#       def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#       def __str__(self):
#           print(self.name,self.age)
#           # return f"{self.name}, {self.age}"
#
# p1 = Person("John", 36)
# print(p1)
#
#
# # #
# # # # The string representation of an object WITH the __str__() function:
# # # #
# # # # class Person:
# # # #   def __init__(self, name, age):
# #
# # # #     self.name = name
# # # #     self.age = age
# # # #
# # # #   def __str__(self):
# # # #     return f"{self.name}({self.age})"
# # # #
# # # # p1 = Person("John", 36)
# # # #
# # # # print(p1)
# #
# class MyClass:
#     x = 5
#     sum = 0
#     def __int__(self,x):
#         self.x=x
#
#     def sum1(self,x):
#         x=x**2
#         return x
#     def display(self,x):
#         print('square = ',self.sum1(x))
#
# obj = MyClass
# obj.display(5)
# # a.Sum(5)1
# # a.display()
#


# class Hello:
#     def sum1(self,x):
#         x=x**2
#         return x
#     def display(self,x):
#         print('square = ',self.sum1(x))
#
# abc = Hello()
# abc.display(2)
#
# #
# #
# 1 create a class student that will take the attendance uisng attendance method,
# attendance should be stored in dictionary with student name
#
# 2 attendance sheet method will display the dictionary

# abc=obj.display()
#
#
# # Python Inheritance
# # Inheritance allows us to define a class that inherits
# # all the methods and properties from another class.
# #
# # Parent class is the class being inherited from, also called base class.
# #
# # Child class is the class that inherits from another class, also called derived class.
#
# # 1)Single Inheritance:
#
# class ParentClass:
#     def display(self,name):
#         return f"My name is {name}"
#
# class ChildClass(ParentClass):
#     pass
#
# a=ChildClass()
# # b=a.display("PKM")
# print(a.display("PKM"))
#
# # 2)Multilevel Inhertiance:
#
# class SuperClass:
#     # Super class code here
#
# class DerivedClass1(SuperClass):
#     # Derived class 1 code here
#
# class DerivedClass2(DerivedClass1):
#     Derived class 2 code here
# obj1=DerivedClass2()

# # 3) Multiple INheritance:
class MostParentClass:
    def dispay(self):
        print("mostparentclass")

class ParentClass:
    def display(self):
        print("parentclass")

class ChildSubClass(MostParentClass,ParentClass):
    def __init__()
        super(.display())
    def display(self):
        super().display()
        # print("child")
    # def display(self):
    #     print("new child")

abc =ChildSubClass()
abc.display()
#
#
#
# # Create a class named Person, with firstname and lastname properties, and a printname method:
#
# # class Person:
# #     def __init__(self, fname, lname):
# #         self.firstname = fname
# #         self.lastname = lname
# #
# #     def __call__(self):
# #         print("call")
# #     def printname(self):
# #         print(self.firstname, self.lastname)
#
# #Use the Person class to create an object, and then execute the printname method:
#
# # x = Person("John", "Doe")
# # x.printname()
# # x()
#
# # Create a class named Student, which will inherit the properties and methods from the Person class:
#
# # class Student(Person):
# #     pass
# #
# # a=Student("abc","ayz")
# # a()
#
# # x = Student("Mike", "Olsen")
# # x.printname()
#
# # class Person:
# #   def __init__(self, fname, lname):
# #     self.firstname = fname
# #     self.lastname = lname
# #   def printname(self):
# #     print(self.firstname, self.lastname)
# #
# # class Student(Person):
# #     def __init__(self,firstname,lastname):
# #         super().__init__(firstname,lastname)
# #         # super().printname()
# #         self.firstname="PKM"
# #         self.lastname="PKM"
# #     def print2(self):
# #         print(self.firstname, self.lastname)
# #       # pass
# # # Use the Student class to create an object, and then execute the printname method:
# # x = Student("Mike", "Olsen")
# # x.printname()
# class Polygon:
#     # Initializing the number of sides
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#     def inputSides(self):
#         self.sides = [1,2,3]
#     # method to display the length of each side of the polygon
#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])
# class Triangle(Polygon):
#     # Initializing the number of sides of the triangle to 3 by
#     # calling the __init__ method of the Polygon class
#     def __init__(self):
#         Polygon.__init__(self,3)
#     def findArea(self):
#         a, b, c = self.sides
#         super().dispSides()
#
# # Creating an instance of the Triangle class
# t = Triangle()
# t.inputSides()
# t.dispSides()
# # Calculating and printing the area of the triangle
# # t.findArea()
#
#
#
# # Method overriding
# # However, what if the same method is present in both the superclass and subclass?
# #
# # In this case, the method in the subclass overrides the method in the superclass. This concept is known as method overriding in Python.
#
# # class Animal:
# #     # attributes and method of the parent class
# #     name = ""
# #
# #     def eat(self):
# #         print(f"I can eat name")
#
# # inherit from Animal
# # class Dog(Animal):
# #     # override eat() method
# #     super.eat()
# #     # def eat(self):
# #     #     super().eat()
# #     #     print("I like to eat bones")
# #
# # # create an object of the subclass
# # labrador = Dog()
# # # # call the eat() method on the labrador object
# # labrador.eat("apple")
#
#
#
# # how to overcome
# #
# #
# # class Animal:
# #     name = ""
# #
# #     def eat(self):
# #         print("I can eat")
# #
# #
# # # inherit from Animal
# # class Dog(Animal):
# #
# #     # override eat() method
# #     def eat(self):
# #         # call the eat() method of the superclass using super()
# #         super().eat()
# #
# #         print("I like to eat bones")
# #
# #
# # # create an object of the subclass
# # labrador = Dog()
# #
# labrador.eat()