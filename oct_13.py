# # brand="brand"
# thisdict = {None: "",
#             "model": [None, "abc"],
#             "year": 1964,
#             # None:1,
#             # "brand":"tata"
#             }
#
# print(thisdict)
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}


my=(1,2)
my2=(3,{1,2},1)
my3=(1,2,4)
# print(thisdict)
# functions:
# print(type(thisdict))
# print(len(thisdict))
# print(tuple(thisdict))
# print(dict())
# print(tuple(zip(my,my2,my3)))



# Accessing dict:

thisdict = {
    "brand": "Ford",
    'model': "Mustang",
    "year": 1964
}
# print(thisdict["model"])
# print(thisdict.get("yea","2023"))
#
# print(list(thisdict.keys())[0])
# # for i in li:
# #     print(i)
# print(thisdict.values())

# x=thisdict.items()
# # print(x)
# # # print(x[0])
# for k in thisdict.items():
#     # j=i
#     print(k,v)
    # print("key",i)
    # print("value", j)
#
#
# # add data to dict:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": "blue",
}
# # #
# x = car.items()
# print(x) #before the change
car["year"] = None
print(car)  # after the change
#
# # change values of dict:
# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # thisdict["year"] = 2018
#
# # update dict:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict.update({"year": 2020},new=1)
# # thisdict['year']=None
# print(thisdict)
# #
# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # thisdict.update({"year": 2020})
#
# # remove items:
# #
# # # 1) pop()
# thisdict = {
#   "0": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x=thisdict.pop("model")
# print(x)
# print(thisdict)

# # # 2)popitem()
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x=thisdict.popitem()
# print(x)
# print(thisdict)
#
# # 3)del
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict['brand']
# print(thisdict)
#
# # 4)clear()
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)
# thisdict['a']=1
# print(thisdict)
#

# # 5)copy()
# first={"a":1}
# second=first
#
# third=first.copy()
# first['b']=2
#
# print(second)
# print(third)

# c=[2,3]
# a=[1,2]
# b=c.copy()
# del a
# print(b)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict2=thisdict
# thisdict3=thisdict.copy()
# thisdict['a']=1
# print(thisdict2)
# print(thisdict3)
#
#
# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # mydict = thisdict.copy()
# # del thisdict
# # # print(thisdict)
# # print(mydict)
#
# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # mydict = dict(thisdict)
# # print(mydict)
#
# # 6) setdefault()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(car)
# print(car.setdefault("color", "None"))
# print(car)
# print(car.setdefault("color", "black"))
# print(car.update({"color": "black"}))
# # # # car.update({"color": "pink"})
# print(car)
# # # print(x)
# #
# # # 7) fromkeys()
# # # x = ('key1', 'key2', 'key3')
# # # y=(1,2)
# # # thisdict = dict.fromkeys(x,y)
# # # thisdict=dict(zip(x,y))
# # # print(thisdict)
#
# # nested dict:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
   "child1":None,
  "child2" : child2,
  "child3" : child3
}

#
print(isinstance(myfamily['child2'],dict))

# print(myfamily["child34"]["name"])
# print(myfamily.get("child34").get('child2'))

# child1 = {
#     "name": "Emil",
#     "year": 2004
# }
# child2 = {
#     "name": "Tobias",
#     "year": 2007
# }
# child3 = {
#     "name": "Linus",
#     "year": 2011
# }
# myfamily = {
#     "child1": "abc",
#     "child2": "abc",
#     "child3": "abc"
# }
#
# # for key,value in myfamily.items():
# #     print(key)
# #     # myfamily[key]="abc"
# #     # print(myfamily)
# #     # print(value)
# #
# #     if "child1" == key or "child2" in key :
# #         print("found")
# #
# # if "child1" in myfamily.keys():
# #     print("yes")
#
# l1=['a', 'b', 'c', 'd', 'e', 'f']
# l2=[1, 2, 3, 4, 5]
# print(dict(zip(l1,l2)))

# zip()
# a=[1,2,3]
# # b=["a","b","c"]
# #
# # print(tuple(zip(a,b)))
#
# # isinstance()
# print(isinstance(a,tuple))


# Write a Python script to concatenate the following dictionaries to create a new one.
#
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
# dict5={}
# for d in [dic1,dic2,dic3]:
#     dict5.update(d)
# print(dict5)

# Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

# Write a Python program to drop empty items from a given dictionary.
# Original Dictionary:
d1={'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

# def value_check(students, n):
# result = all(x == n for x in students.values())
    # return result

dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
# print("Original Dictionary:")
# print(dict1)
# print("New Dictionary after dropping empty items:")
# dict1 = {key:value for (key, value) in dict1.items() if value is not None}
# print(dict1)

dict2={}
for k,v in dict1.items():
    if v is not None:
        dict2[k] = v
print(dict2)