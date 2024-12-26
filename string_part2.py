# String Method 1:

# upper() and lower()
string_var = "This is string part 2"

print(string_var.upper())
print(string_var.lower())

# .isupper() and .islower()

string_var2 = "This is string part 2"

print(string_var.islower())
print(string_var.isupper())

# Aditional extensions:

# .isalpha() - checks is only letters
# .isalnum() - checks is only number and letters
# .isdecimal() - checks is only number.
# .isspace() - checks is only space
# .istitle() - checks is only title case.

print("batman".isalpha()) # Result: True
print("batman".isalnum()) # Result: True
print("batman".isdecimal()) # Result: False
print("123".isdecimal()) # Result: True
print("123.1".isdecimal()) # Result: False
print(" ".isspace()) # Result: True
print("The Empire Is Back".istitle()) # Result: True

print("this is title".title()) # Result: This Is Title

# .startswith()
# .endswith()

print("I am batman".startswith("I")) # Result: True
print("I am batman".startswith("I am")) # Result: True
print("I am batman".endswith("batman")) # Result: True

# join()

print("".join(['one', 'two', 'three'])) #Result: onetwothree
print(" ".join(['one', 'two', 'three'])) #Result: one two three
print(",".join(['one', 'two', 'three'])) #Result: one,two,three
print(":".join(['one', 'two', 'three'])) #Result: one:two:three
print("-".join(['one', 'two', 'three'])) #Result: one-two-three

# split()

print('I am batman'.split()) #Result: ['I', 'am', 'batman']
print('apple, orange, mango'.split(','))  #Result: ['apple', ' orange', ' mango']
print('someKey:value'.split(':')) #Result: ['someKey', 'value']


