# Statements

# If statement:

if True:
    print("Print this!") # Result: this will print

if False:
    print("Not Print this!") # Result: this will not print

var_1 = 100
var_2 = 1000

if var_1 == var_2:
    print("This is same...")

veg = input("Enter vegetable name: ")

if veg == "potato":
    print("You choosed potato!")

# If the condition is true,
# then only compiler allow to execute inside of if block codes
# Otherwise skip the block and move to next line.
# 
# Example:
#
# line 1
# line 2
#  if (Some condition): (line 3)
#     line 3
#     line 4
#     line 5
# line 6
# line 7
#
# Compiler execute the code line by line that stats from the line 1
# then when comes to line 3 it will check the condition True or False
# If True, compiler will execute line 3, 4 and 5
# If False, skip the line 3,4, and 5, and goes to line 6 and 7.
    
#-------------------------------------------------------#
    
veg = input("Enter vegetable name: ")

if veg == "potato":
    print("Wow! you choosed my favourite potato :)")
else:
    print("You choosed " + veg)

# If the condition is true,
# then compiler will execute the inside of if block codes
# If False, it will execute the else block
# 
# Example:
#
# line 1
# line 2
#  if (Some condition): (line 3)
#     line 3
#     line 4
#     line 5
# else:
#     line 6
#     line 7
# line 8
# line 9
#
# Compiler execute the code line by line that stats from the line 1
# then when comes to line 3 it will check the condition True or False
# If True, compiler will execute line 3, 4 and 5
# If False, it will come into else block and execute line 6 and 7
# then execute line 8 and 9
    
#-------------------------------------------------------#
    
# Nested IF else:
    
veg = input("Enter vegetable name: ")
dish = input("Enter favorite dish using the vegetable: ")

if veg == "potato":
    if dish == "potato fry":
        print("Wow! you choosed my favourite potato and dish :)")
    else:
       print("Wow! you choosed my favourite potato :)") 
elif veg == "onion" : 
    print("Wow! you choosed my favourite onion :)") 
else:
    print("You choosed " + veg)

# Another example for pratice:
    
score = int(input("Please enter the student's score. "))
 
if score >= 90:
    print("This student's score of " + str(score) + " is an A.")
else:
    if score >= 80:
        print("This student's score of " + str(score) + " is a B.")
    else:
        if score >= 70:
            print("This student's score of " + str(score) + " is a C.")
        else:
            if score >= 60:
                print("This student's score of " + str(score) + " is a D.")
            else:
                print("This student's score of " + str(score) + " is a F.")

#-------------------------------------------------------#
                
# Truthy and Falsy value
                
veg = input("Enter vegetable name: ")

if veg:
    print("You entered a value thanks!")
else: 
    print("You didnt enter any string")

print(bool("apple")) # True

print(bool(0)) # False