print("---------------------# Tuple ----------------------")
# Tuple is similer to list but diffrenc is the items a packed with ().
# Tuple does not allow to change the value of item.
tuple_1 = tuple([1,3,4,5,6,7,8, "q"])
print(tuple_1) # Result: (1, 3, 4, 5, 6, 7, 8, 'q')

tuple_2 = tuple({"a":1,"b":4, "c":7})
print(tuple_2) # Result: ('a', 'b', 'c')


tuple_3 = (1,2,3,4,5,6,7,8,9)
print(tuple_3[2:5])
print(tuple_3[:5])
print(tuple_3[5:])

#Result:
# (3, 4, 5)
# (1, 2, 3, 4, 5)
# (6, 7, 8, 9)

print("---------------------# Tuple loop and step ----------------------")

tuple_4 = (1,2,3,4,5,6,7,8,9)
print(tuple_4[::2]) # stride length of 3
print(tuple_4[1::2]) # evens only
print(tuple_4[7::-1]) # bacward from the 8
print(tuple_4[8::-2]) # odds only backwards

print("---------------------# Nested Tuples ----------------------")

tuple_5 = ((1,2,3,4), (5,6,7,8), (9,0,1,2))
print(tuple_5[0][1]) # Result: 2

tuple_6 = (1,2,3,4,5,6,7,8,9,1) # number of 1 value present in tuple_6 variable.
print(tuple_6.count(1)) # 2

# to get the idex of the item
print(tuple_6.index(5)) # 4





