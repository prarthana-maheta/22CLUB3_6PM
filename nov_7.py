# print(thisdict["model"])
# print(thisdict.get("yea","no"))
# print(thisdict.keys())
# print(thisdict.values())
# x=thisdict.items()
# .copy(),zip(),update()

1. Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}



2. Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


3. Write a Python script to check whether a given key already exists in a dictionary.

4. Write a Python program to iterate over dictionaries using for loops.

5. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

6. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


7. Write a Python program to create a flat list of all the values in a flat dictionary.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Create a flat list of all the values of the said flat dictionary:
values=[19, 20, 21, 20]
keys=["",""]


8. Write a Python program to combine two lists into a dictionary. The elements of the first
one serve as keys and the elements of the second one serve as values. Each item in the first list must
be unique and hashable.
Sample Output:
Original lists:
['a', 'b', 'c', 'd', 'e', 'f']
[1, 2, 3, 4, 5]
Combine the values of the said two lists into a dictionary:
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}




9.  Write a Python program to find all keys in a dictionary that have the given value.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Find all keys in the said dictionary that have the specified value:
['Roxanne', 'Betty']



10. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}













# 1 ans:
# d = {0:10, 1:20}
# print(d)
# d.update({2:30})
# print(d)


# 2 ans
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# print(dic4)


# 3 ans
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(x):
#   if x in d:
#       print('Key is present in the dictionary')
#   else:
#       print('Key is not present in the dictionary')
# is_key_present(5)
# is_key_present(9)


# 4 ans
# d = {'x': 10, 'y': 20, 'z': 30}
# for dict_key, dict_value in d.items():
#     print(dict_key,'->',dict_value)


# 5 ans
# n=int(input("Input a number "))
# d = dict()
#
# for x in range(1,n+1):
#     d[x]=x*x
#
# print(d)


# 6 ans
# d=dict()
# for x in range(1,16):
#     d[x]=x**2
# print(d)


# 7 ans
# def test(flat_dict):
#   return list(flat_dict.values())
# students = {
#   'Theodore': 19,
#   'Roxanne': 20,
#   'Mathew': 21,
#   'Betty': 20
# }
# print("\nOriginal dictionary elements:")
# print(students)
# print("\nCreate a flat list of all the values of the said flat dictionary:")
# print(test(students))


# 8 ans
# def test(keys, values):
#   return dict(zip(keys, values))
#
# l1 = ['a', 'b', 'c', 'd', 'e', 'f']
# l2 = [1, 2, 3, 4, 5]
# print("Original lists:")
# print(l1)
# print(l2)
# print("\nCombine the values of the said two lists into a dictionary:")
# print(test(l1, l2))


# 9 ans
# def test(dict, val):
#   return list(key for key, value in dict.items() if value == val)
#
# students = {
#   'Theodore': 19,
#   'Roxanne': 20,
#   'Mathew': 21,
#   'Betty': 20
# }
#
# print("\nOriginal dictionary elements:")
# print(students)
# print("\nFind all keys in the said dictionary that have the specified value:")
# print(test(students, 20))


# 10 ans
# from collections import defaultdict, Counter
str1 = 'w3resource'
my_dict = {w:1,3:1,r:2}
for letter in str1:
    # letter=w
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)