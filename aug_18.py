# looping through string
# a="1234"
# for x in a:
#     print(x)

# looping through list
# fruits = ["apple", "1", "cherry"]
# for x in fruits:
#     for y in x:
#         print(y)
#     print(x)




# With the break statement we can stop the
# loop before it has looped through all the items:

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#
#   if x == "banana":
#     break
#     print(x)



# Exit the loop when x is "banana", but
# this time the break comes before the print:
#
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     for y in x:
#       if x == "banana":
#         print(y)
#         break
#         print(y)
#     print(x)


# With the continue statement we can stop
# the current iteration of the loop, and continue
# with the next:

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     pass
#
#
# if 1==1:
#     pass
# fruits = ["apple", "banana", "cherry"]
# for x in fruits[::-1]:
#     for y in x:
#         print(y)
#   # if x == "banana":
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
# # for x in reversed(fruits):
# #   # if x == "banana":
# #     print(x)
#
# # print(list(reversed(fruits)))
# print(fruits)
# # print(fruits.reverse())
# fruits.reverse()
# print(fruits)
# for loops cannot be empty, but if you for some
# reason have a for loop with no content, put in
# the pass statement to avoid getting an error.
#

for x in range(0,11):
    print(x)

# having an empty for loop like this,
# would raise an error without the pass statement

# pop()


# The range()
# function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# for x in range():
#   print(x)

# for x in range(-1,1,3):
#   print(x)


#start,stop,increment
# for x in range(2, 30, 3):
#   print(x)
#
# Example 1: Print the first 10 natural numbers using for loop.
# Example 2: Python program to print all the even numbers within the given range.
# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.




# Example 4: Python program to calculate the sum of all the odd numbers within the given range.
# Example 5: Python program to print a multiplication table of a given number
# Example 6: Python program to count the total number of digits in a number.
# Example 7: Python program that accepts a word from the user and reverses it.
# Example 8: Python program to count the number of even and odd numbers from a series of numbers.
# Example 9: Python program to find the factorial of a given number.








#######################1############
# # between 0 to 10
# # there are 11 numbers
# # therefore, we set the value
# # of n to 11
# n = 11
#
# # since for loop starts with
# # the zero indexes we need to skip it and
# # start the loop from the first index
# for i in range(1, n):
#     print(i)



#######################2########################
# # if the given range is 10
# given_range = 10
#
# for i in range(given_range):
#
#     # if number is divisble by 2
#     # then it's even
#     if i % 2 == 0:
#         # if above condition is true
#         # print the number
#         print(i)


################3##############

# # if the given number is 10
# given_number = 10
#
# # set up a variable to store the sum
# # with initial value of 0
# sum = 0
#
# # since we want to include the number 10 in the sum
# # increment given number by 1 in the for loop
# for i in range(1, given_number + 1):
#     sum += i
#
# # print the total sum at the end
# print(sum)



###############4##############

# if the given range is 10
given_range = 10

# set up a variable to store the sum
# with initial value of 0
sum = 0

for i in range(0,given_range+1):

    # if i is odd, add it
    # to the sum variable
    if i % 2 != 0:
        # sum=sum+i
        sum += i

# print the total sum at the end
print(sum)


################5#####################


# if the given range is 10
given_number = input()

for i in range(11):
    print(given_number,"X",i,"=",given_range*i)
    print(f"{given_number}x{i}={given_number * i}")


####################6#####################


# if the given number is 129475
given_number = 12345
# for i in given_number:
#     print(i)
# # since we cannot iterate over an integer
# # in python, we need to convert the
# # integer into string first using the
# # str() function
given_number = str(given_number)
#
# # declare a variable to store
# # the count of digits in the
# # given number with value 0
count = 0
#
for i in given_number:
    if i.isdigit():
        count += 1
#
# # print the total count at the end
print(count)




# gn=list(given_number)
# print(len(gn))



#######################7#################

# input string from user
given_string = input()
print(given_string[::-1])

# an empty string variable to store
# the given string in reverse
reverse_string = "cba"
# abc
# iterate through the given string
# and append each element of the given string
# to the reverse_string variable
for i in given_string:
    reverse_string = i + reverse_string

# print the reverse_string variable
print(reverse_string)


list(given_number.reversed)
reverse()




#################10##################

given list of numbers
# num_list = list(input())
# print(type(num_list))
# print(num_list)
# iterate through the list elemets
# using for loop
e=0
o=0
for i in num_list:

    # if divided by 2, all even
    # number leave a remainder of 0
    if i % 2 == 0:
        e+=1
        print(i, "is an even number.")

    # if remainder is not zero
    # then it's an odd number
    else:
        o+=1
        print(i, "is an odd number.")

print(o,e)


######################9#################


# given number
given_number = 5

# since 1 is a factor
# of all number
# set the factorial to 1
factorial = 1
126
# iterate till the given number
for i in range(1, given_number + 1):
    factorial = factorial * i
    print(factorial)

print("The factorial of ", given_number, " is ", factorial)