# Loop

# while loop:

counter = 10
while counter >= 1:
    #print(" ===> " + str(counter))
    counter -= 1

# Output:
#  ===> 0
#  ===> 1
#  ===> 2
#  ===> 3
#  ===> 4
#  ===> 5

# EXAMPLE

# pos_int is a variable which holds a user entered integer.
pos_int = int(input("Please enter a positive integer."))

# This variable stores the initial value of pos_int before it is used in the loop so
# that later it can be used to display pos_int's initial value in the output.
int_init = pos_int
# This is a variable which will be used to hold the sum of all the integers from pos_int.
summed = 0
# The while loop will run while pos_int's stored integer value is greater than 0
while pos_int > 0:
    # This is the equivalent of summed = summed + pos_int
    # In other words: new value of summed = old value of summed + new value of pos_int
    summed += pos_int
    # This will decrement pos_int so that pos_int will eventually equal 0 and the while
    # loop will stop running its code.
    pos_int -= 1
 
#print(int_init)  # displays the initial value of pos_int
#print(summed)    # displays the sum of integers from pos_int

#----------------------------------------------------------------#

# For loop:

name = "Hello World!"

for letter in name:
    print(letter)

#EXAMPLE
    
char = input("Enter your string: ")

count = 0

for letter in char:
    count += 1

print(char)
print(count)

#----------------------------------------------------------------#

# range() - data type range

range_var = range(5) # 5 num count

for char in range_var:
    print(char)

# Output:
# 0
# 1
# 2
# 3
# 4

range_var_2 = range(5, 10) # number starts from number 5 and ends before 10

for char in range_var_2:
    print(char)

# Output:
# 5
# 6
# 7
# 8
# 9

print("range(2, 20, 2)")
range_var_3 = range(6, -1, -2) # number 'starts from number 5' and 'ends before 10' and 'print second number'

for char in range_var_3:
    print(char)

# Output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18