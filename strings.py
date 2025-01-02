print("------------------------ # Strings ---------------------------")

string_var = "This is me!"

print("------------------------ # Access by index ---------------------------")
print(string_var[8]) # Output: "m"
print(string_var[9]) # Output: "e"

print("------------------------ # String slicing ---------------------------")
# String slicing - sequence[start:stop:step]
text = "Apple"
print(text[3:])   # Output: "le"
print(text[:3])   # Output: "App" (characters before index 3)
print(text[1:4])  # Output: "ppl" (characters from index 1 to 3)
print(text[::2])  # Output: "Ape" (every 2nd character)

print("------------------------ # Concatenation  ---------------------------")
concatenation = "R2" + "-" + "D4"
print(concatenation)
print(concatenation[2])
print(concatenation[1:4])

print("------------------------ ## Strings Exercises  ---------------------------")
to_slice = "Just do it!"
print(to_slice[10])   # prints "!"
print(to_slice[5:7])  # prints "do"
print(to_slice[8:])   # prints "it!"
print(to_slice[:4])   # prints "Just"
print("Don't " + to_slice[5:])  # prints "Don't do it!"

#-------------------------------------------------------#

print("------------------------ #type() and str() ---------------------------")

exp_1 = "string"
exp_2 = 100
exp_3 = 13.0
exp_4 = True
exp_5 = str(exp_2)

print(type(exp_1))
print(type(exp_2))
print(type(exp_3))
print(type(exp_4))
print(type(exp_5))

#-------------------------------------------------------#

print("------------------------ # Escape Sequence ---------------------------")

# "\t" - Make horizontal space
# "\n" - Make a new line
# \' and \'' - Make a ' and "" inside the string value
# "\\" - to add '\' into the string

#-------------------------------------------------------#

print("------------------------ # Input ---------------------------")

name = input("Enter your name: ")
print("Your name is " + name + "." )

#-------------------------------------------------------#

print("------------------------ # int() and float() ---------------------------")

int_1 = "100"
float_1 = "1.6"

print(int(int_1))
print(float(float_1))