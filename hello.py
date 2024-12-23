# Variables
string_1 = "Hello!"      # String
int_1 = 1                # Integer
float_1 = 1.5            # Float
bool_1 = True            # Bolean
string_1 = string_1 + " World"

# Math Operator
add_var = 1 + 10         # 11
sub_var = 29 - 39        # -10
div_var = 1.2 / 3.10     # 0.3870967741935484
mult_var = 30 * 50       # 1500

# Exponential
ex_var = 40 ** 10         # 4x4 = 16

# Floor Division
floor_var = 16 // 5      # 16/5=3.5 to get the int use '//' operator.

# Assignment Operators
ass_1 = 5
ass_2 = 5
ass_2 += ass_1           # do 5+5 add operation and reassign it to ass_2 variable
ass_2 **= ass_1 

# Order of Operatons
# 1.() - execute first
# 2.** - second prio
# 3.%, /, //, and * 
# 4. + and -
# EX:
order_of_operation = (10 * 5) + 40 ** 10 * 11 // 34 - 1 % 5
# Step 1: 50 + 40 ** 10 * 11 // 34 - 1 % 5
# Step 2: 50 + 10485760000000000 * 11 // 34 - 1 % 5
# Step 3: 50 + 3392451764705882 - 1 (Left to Right)
# Step 4: 3392451764705931

data = 15 / 3 * 2 * 2 - (3 + 4)
# 15 / 3 * 2 * 2 - 7
# 15 / 3 * 2 * 2 - 7 ('/' and '*' have same prio so its comes left to right)
# 5 * 2 * 2 - 7
# 10 * 2 - 7
# 20 - 7
# 13

# More on float
float = (123 + 223) / 100
# print(float) - 3.46
# print(round(float)) - 3
# print(round(float, 1)) - 3.4
# print(round(float, 2)) - 3.46

print(16.68 * 12)