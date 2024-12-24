# Statements

# If statement:

if True:
    print("Print this!")

if False:
    print("Not Print this!")

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