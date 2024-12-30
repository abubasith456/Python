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


#-------------------------------------------------------#

# rjust() and ljust() - Right Just and Left Just

# Add a space in front of the string and needs to give the length
print("Hello world".rjust(15)) # Result:     Hello world
# Add a space value as * in front
print("Hello world".rjust(15, "*")) # Result: ****Hello world

 # Add a space in end of the string and needs to give the length
print("Hello world".ljust(15)) # Result: Hello world    
 # Add a space value as - in end
print("Hello world".ljust(15, "-")) # Result: Hello world----

# center()

# Add a space eventually for front and back of the string and needs to give the length
print("Hello world".center(15))  # Result:   Hello world  
# Add a space value as * in front
print("Hello world".center(15, "*")) # Result: **Hello world**

# split()

print("Hello World!!!!!")
# Removes the character
print("Hello World!!!!!".strip("!")) # Result: Hello World
print("Hello World!!!!!".rstrip("!")) # Result: Hello World
print("Hello World!!!!!".lstrip("!")) # Result: Hello World!!!!!

print("BlueYellowBlueYellow".lstrip("Blue")) # Result: YellowBlueYellow
print("BlueYellowBlueYellow".rstrip("Yellow")) # Result: BlueYellowBlu
print("blueblueyellowblue".strip("eulb")) # Result: yellow

# replace()

print("Hello World!".replace("!", "?")) # Result: Hello World?

# len() function

print(len("Hello World!")) #Result: 12


# Excercise
data = "Hello world!"
dataLeng = len(data)
reversed = ""

while (dataLeng >= 1):
    reversed += data[dataLeng - 1]
    dataLeng -= 1
    
print(reversed) # Result: !dlrow olleH

# formate() - comble the text by pass the strings as parms.

name = input("Enter your name: ")
age = input("Enter your native place: ")

print("My name is {}, I am coming from {}".format(name, age)) # Result: My name is Abu, I am coming from Chennai


