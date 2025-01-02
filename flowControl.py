print("------------------------ # Flow Controll ---------------------------")

# Comparison Operator (only returns true or false)

# < - Less than
# > - Greater than
# <= - Less than or equal to
# >= - Greater than or equal to
# != - Not equal to
# == - Equal to

var_1 = 1 > 2   #Result: False
var_2 = 3 < 2   #Result: False
var_3 = 4 <= 5  #Result: True
var_4 = 4 >= 4  #Result: True
var_5 = 4 != 6  #Result: True
var_6 = 4 == 5  #Result: False

var_7 = 4.0 == 4 #Result: True 

print(var_1)
print(var_2)
print(var_3)
print(var_4)
print(var_5)
print(var_6)
print(var_7)

#-------------------------------------------------------#

print("------------------------ # Boolean Operators: ---------------------------")

# and 
# or
# not

print("------------------------ # and: ---------------------------")

# and: 
# True and True = True
# True and False = False
# False and True = false
# False and False = False

var_8 = 4 == 5 and 4 == 4  #Result: False
var_9 = 4 == 4 and 4 == 4  #Result: True
var_10 = 4 == 5 and 4 == 6 #Result: False

print(var_8)

print("------------------------ # or: ---------------------------")
# True and True = True
# True and False = True
# False and True = True
# False and False = False

var_11 = 4 == 5 or 4 == 4  #Result: True
var_12 = 4 == 4 or 4 == 4  #Result: True
var_13 = 4 == 5 or 4 == 6 #Result: False

print("------------------------ # not (Vise versa): ---------------------------")

# not True = False
# not False = True

var_14 = not 4 == 5 #Result: True
var_15 = not 5 == 5 #Result: False

print(var_14)
print(var_15)

