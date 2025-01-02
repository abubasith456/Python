print("---------------------# Sets ----------------------")
# set also samw like a list but its does not contain the duplicate value.
# same like dictionary this is unordered.

set_1 = {1,2,3,4,5,6,7,8, 8}
set_2 = set({0,9,8,7,6, 0})

print(set_1) # Result: {1, 2, 3, 4, 5, 6, 7, 8}
print(set_2) # Result: {0, 6, 7, 8, 9}

# print(set_1[0]) -  'set' object is not subscriptable


print("---------------------# Set add() method ----------------------")

set_1.add(10)
print(set_1) # result: {1, 2, 3, 4, 5, 6, 7, 8, 10}

print("---------------------# Set remove() method ----------------------")

set_1.remove(5) 
print(set_1) # Result: {1, 2, 3, 4, 6, 7, 8, 10}

print("---------------------# Set discard() method ----------------------")

set_1.discard(11) # this not cause the any exception
print(set_1) # Result: {1, 2, 3, 6, 7, 8, 10}

print("---------------------# Set clear() method ----------------------")

set_1.clear() # clear the set value
print(set_1) # Result: {1, 2, 3, 6, 7, 8, 10}

print("---------------------# Set copy() method ----------------------")

# memory address chnaged when you takes the copy of the set
set_3 = set({0,9,8,7,6, 0})
set_4 = set_3.copy()

print(set_3 is set_4) # False

print("---------------------# Set union() method ----------------------")

set_5 = set({1,2,3,4,5})
set_6 = set({6,7,8,9,0})
# Combine the 2 set into single
print(set_5.union(set_6)) # Result: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print("---------------------# Set intersection() method ----------------------")
# return the common data

set_7 = set({0,2,3,4,5})
set_8 = set({6,7,3,9,0})

print(set_7.intersection(set_8)) # Result: {0, 3}
# We can use the '&' keyword to do this process
print(set_7 & set_8) # Result: {0, 3} 

print("---------------------# Set substraction() method ----------------------")

# remove the common items and return the other value.
print(set_7 - set_8) # Result: {2, 4, 5}

print("---------------------# Set difference() method ----------------------")

# remove the common items and return the other value. (same like substraction)
print(set_7.difference(set_8))

print("---------------------# Set comprehensions ----------------------")

# can do the operation insode the set by below
set_9 = {even + 2 for even in range(2, 11, 2)}
print(set_9) #Result: {4, 6, 8, 10, 12}

set_10 = {text.lower() for text in "APPLE"}
print(set_10) #Result: {'a', 'e', 'l', 'p'}
