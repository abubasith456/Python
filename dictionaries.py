print("------------------------ # Dictionariies - Unordered ---------------------------")


dic_1 = { 1: "Test", 2: "Text", 3: "The" }
dic_2 = { 3: "The",1: "Test", 2: "Text"}

print(dic_1[1]) # Result: Test

print( dic_1 == dic_2 ) # Result: True 
#In array data set should be in same order, but in dictionary it checks only the key and value match.

print(1 in dic_2) # Result: True 

print(1 not in dic_2) # Result: False 


# Dictionary Methods 1 (keys(), values(), items() and get()):

print(dic_2.keys()) # Result: dict_keys([3, 1, 2])
print(dic_2.values()) # Result: dict_values(['The', 'Test', 'Text'])
print(dic_2.items()) #Result: dict_items([(3, 'The'), (1, 'Test'), (2, 'Text')])

for key, value in dic_2.items():
    print("Key: " + str(key))
    print("Value: "+ value)

# Result: 
    
# Key: 3
# Value: The
# Key: 1
# Value: Test
# Key: 2
# Value: Text
# Text

print(dic_2.get(2)) # Result: Text

print("------------------------ Dictionary Methods 2 (fromkeys(), popu()) ---------------------------")
print("-------------------# fromkeys() - To create the new key pair dictonariy.--------------------------------")

# fromkeys() - To create the new key pair dictonariy.
dic_3 = {}.fromkeys(["SomeKey"], "Some value!")
print(dic_3) # Result: {'SomeKey': 'Some value!'}
dic_4 = {}.fromkeys("Some", "Some value!")
print(dic_4) # Result: {'S': 'Some value!', 'o': 'Some value!', 'm': 'Some value!', 'e': 'Some value!'}

print("-------------------------# pop() - Remove the key pair from the entity.--------------------------")
dic_5 = { "key1": "value1","key2": "value2", "key3": "value3"}
dic_5.pop("key2")
print(dic_5) # Result: {'key1': 'value1', 'key3': 'value3'}

print("--------------------# popitem() - removes the last index key pair form the dictionary-------------------")
dic_5.popitem()
print(dic_5) # Result: {'key1': 'value1'}

print("--------------------------# clear() - clear the dictionary data-------------------------")
dic_6 = { "key5": "value5","key6": "value6", "key7": "value7"}
dic_6.clear()
print(dic_6) # Result: {}

print("-------------------------# copy() - take copy of the dictionary data--------------------------")
dic_7 = { "key5": "value5","key6": "value6", "key7": "value7"}
dic_8 = dic_7.copy()
dic_8["key6"] = "TestData"
print(dic_8)
print(dic_7)

# Result:
# {'key5': 'value5', 'key6': 'TestData', 'key7': 'value7'}
# {'key5': 'value5', 'key6': 'value6', 'key7': 'value7'}

print("-------------------------# update() - update the existing dictionary data--------------------------")
dic_9 = { "key5": "value5","key6": "value6", "key7": "value7"}
dic_10 = {"key10": "value10"}
print(dic_9)
dic_9.update(dic_10)
print(dic_9)

#Result:
# {'key5': 'value5', 'key6': 'value6', 'key7': 'value7'}
# {'key5': 'value5', 'key6': 'value6', 'key7': 'value7', 'key10': 'value10'}

print("---------------------------------------------------")

dic_11 = { "key5": "value5","key6": "value6", "key7": "value7"}
dic_12 = {"key10": "value10"}
dic_11.update(dic_12)
dic_11["key10"] = "TestData"
print(dic_11)
dic_11.update(dic_12)
print(dic_11)

# Result:
# {'key5': 'value5', 'key6': 'value6', 'key7': 'value7', 'key10': 'TestData'}
# {'key5': 'value5', 'key6': 'value6', 'key7': 'value7', 'key10': 'value10'}

print("--------------------------# setDefault() - set the key and value as default its does not change-------------------------")
# if the setDefault value not exist in the dictinory it will be added

dic_13 = {"Apple": "iPhone", "Samsung": "Tablet"}
dic_13.setdefault("Lenovo", "Laptop")
dic_13.setdefault("Lenovo", "TAB")
print(dic_13) #Result: {'Apple': 'iPhone', 'Samsung': 'Tablet', 'Lenovo': 'Laptop'}

print("--------------------------# dic() - To create the dictionary key pair-------------------------")

dic_14 = dict(a=1,b=2,c=3,d=4)
print(dic_14) # Result: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


