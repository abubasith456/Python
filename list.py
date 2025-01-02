print("------------------------ # List ---------------------------")

list_1 = ["apple", "orange", "orange"] 
list_2= [["Chennai", "Tambaram"], ["Cudalur", "Mayladuthurai"], ["Mayladuthurai", "Thiruvarur"]]
list_3 = [1,2,3,4,5]
list_4 = [[2,3], [4,5]] # 2D list
list_5 = [True, False, True]
list_6 = [1, "Text", 1.0, True, [1,2,3]] # mixed list

print(list("Hello"))

print("------------------------ # in and not in - list contains item or not ---------------------------")

print(1 in list_3) # Result: True
print(8 not in list_3) # Result: True

print("------------------------ # indexces and slice ---------------------------")

print(list_1.index("orange")) # Result: 1

print(list_6[2]) # Result: 1.0
# 2D list
print(list_4[1][1]) # Result: 5

print(list_1[1][0]) # Result: o

print(list_3[-1]) # Result: 5 - Gets the last item from the list

print("------------------------ # slice ---------------------------")

print(list_3[:2]) # Result: [1, 2]
print(list_3[1:4]) # Result: [2, 3, 4]
print(list_3[3:]) # Result: [4, 5]

print("------------------------ # Reassigning list item value ---------------------------")

list_3[3] = 10
print(list_3) # Result: [1, 2, 3, 10, 5]

list_3[1:4] = [4,3,2]
print(list_3) # Result: [1, 4, 3, 2, 5]

print("------------------------ # del and list methods ---------------------------")

listDel = [1,2,3,4,5,6]
del listDel[3]
print(listDel) # Result: [1, 2, 3, 5, 6]

listRemove = ["apple", "orange", "banana"] 
listRemove.remove("banana")
print(listRemove) # Result: ['apple', 'orange']

print("------------------------ # append() ---------------------------")

pets = ["dog", "cat", "tiger"]
pets.append("snake")
print(pets) # Result: ['dog', 'cat', 'tiger', 'snake']

pets.insert(1, "monkey")
print(pets) # Result: ['dog', 'monkey', 'cat', 'tiger', 'snake']

print("------------------------ # sort() ---------------------------")

sorted_number= [123, 4.6, 232323, -1, -1234]
sorted_number.sort()
print(sorted_number) # Result: [-1234, -1, 4.6, 123, 232323]

print("------------------------ # pop() ---------------------------")
popFromItems = [123, 4.6, 232323, -1, -1234]
temp = popFromItems.pop()
print(popFromItems) #Result: [123, 4.6, 232323, -1]

# List VS Strings
# List is mutable
# Strins is imutable

print("------------------------# Refferences ---------------------------")
exp_6 = [1,2,3,4,5]
exp_7 = exp_6
exp_7[1] = 10
print(exp_6)
print(exp_7)

#Result: 
#[1, 10, 3, 4, 5]
#[1, 10, 3, 4, 5]

print("------------------------# Creates the different memory allocation and reffernce ---------------------------")
import copy
exp_8 = [1,2,3,4,5]
exp_9 = copy.deepcopy(exp_8)
exp_9[1] = 10
print(exp_8)
print(exp_9)

#Result:
# [1, 2, 3, 4, 5]
# [1, 10, 3, 4, 5]


















