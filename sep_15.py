#
#
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)


# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#
# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#
# Allow Duplicates


# print(type(thistuple))
# print(len(thistuple))
#
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# # tuple(thistuple)
# # print(thistuple[2:5:-1])
# print(thistuple[-5:-2:-1])

# check if present
thistuple = ("apple", "cherry", "apple")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
if "ch" in thistuple:
    print("yes, 'cherry' in ")
elif "ple" in thistuple:
    print("NO")
else:
    print("2345")




# change tuple value update tuple
#
x = ("apple", "banana", "cherry")
y = list(x)
# x[0]="sbc"
# print(x)
# print(y)
# y=[x]
# print(y)
#
# # #
# y.insert(0,"kiwi")
# y[0] = "kiwi"
# # #
# print(y)
# x = tuple(y)
# # #
# print(x)


# add items to tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#
#
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)



# # unpack tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "apple", "cherry", "strawberry", "raspberry")

# (a,*red) = fruits
#
# print(green)
# print(yellow)
# print(red)

print(fruits.count("apple"))