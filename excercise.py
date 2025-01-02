# Programming Challenge: Word Counter

str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."


def get_words_count(text):
    words = ""
    wordsCount = 1
    for i in text:
        words += i
    for j in words:
        if (j == " "):
            wordsCount += 1
    return wordsCount

print(get_words_count(str_2))


# Dictionary:

# Do all of this in a .py file in Pycharm.

# use .fromkeys() to create a dictionary that has the consonants from 
#the alphabet as its keys and the string "consonant" as the value for each of those keys.  
#Only use lower case letters for the consonants.  "y" counts as a consonant for this exercise.  
#Use a for loop and the .items() method to print each of those key: value pairs on a different line.  
#For example, the first 3 lines in the output should be the following:

# b consonant

# c consonant

# d consonant

# paste this dictionary into your .py file then pop and print "Big Mac" from it

# fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
# use .popitem() to remove the last key: value pair from the dictionary assigned to fast_food_items then print new fast_food_items dictionary.

for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
    print(key, value)
 
fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))
 
fast_food_items.popitem()
print(fast_food_items)

#--------------------------------------------------------------------------------------#

# Do all of this in a .py file in Pycharm.

# 1. paste these 2 dictionaries into your file

# internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# another_one = {"shroud": "Twitch"}
# use .update() to add the contents of another_one to internet_celebrities.

# 2. create a variable and assign it a copy of internet_celebrities.

# 3. use the .clear() method to get rid of the contents of internet celebrities.

# 4. print internet_celebrities.

# 5. print the variable you created in step 3.

internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)  # 2
gamers = internet_celebrities.copy()  # 3
internet_celebrities.clear()  # 4
print(internet_celebrities)  # 5
print(gamers)  # 6

