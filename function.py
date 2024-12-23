# Defining a functions

def function():
    print("This is function!")

function()

# function with parameter with default value

def function(parameter = "1"):
    print("The number is " + parameter)

function("10")

# function with return value

def function(parameter = "1"):
    return "The number is " + parameter

print(function())

# Import Modules

# Generic Import:
import random
print(random.randint(1, 100))

# Function import
from random import randint
print(randint(1, 100))

# Universal import
from random import *
print(random())

# Variable Scope

# - Local Variable dont access on global scope.
# - Global Variable can access on Local scope.
# - Local variable in function coudln access on another function.

global_var = "This is global variable"

def function_1():
    local_var_1 = "This is local variable 1"
    print(global_var + "\n" + local_var_1)

def function_2():
    local_var_2 = "This is local variable 2"
    print(global_var + "\n" + local_var_2)

function_1()
function_2()
