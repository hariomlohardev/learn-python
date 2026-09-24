"""
=====================================================
   PYTHON PRACTICE FILE - VARIABLES & DATA TYPES
=====================================================

Welcome! This file will help you test whether you have
understood the basics of Variables and Data Types in Python.

Instructions:
1. Read each comment carefully.
2. Wherever you see "# TODO", write your own code below it.
3. Do NOT delete the comments, they are there to guide you.
4. Once done, run the file and check if the output matches
   what is expected.
5. Submit this completed file in the comment section of the
   blog post.

Good luck! 🐍
=====================================================
"""


"""
-----------------------------------------------------
SECTION 1: CREATING VARIABLES
-----------------------------------------------------
A variable is used to store data/information so that it
can be used later in the program.

Example:
name = "Alex"
age = 20
"""

# TODO: Create a variable called 'my_name' and store your name in it


# TODO: Create a variable called 'my_age' and store your age in it


# TODO: Print both variables using print()



"""
-----------------------------------------------------
SECTION 2: INTEGER (int)
-----------------------------------------------------
Integers are whole numbers (no decimal point).
Example: 5, -10, 100
"""

# TODO: Create a variable called 'apples' and assign it a whole number


# TODO: Print the type of the 'apples' variable using type()



"""
-----------------------------------------------------
SECTION 3: FLOAT (float)
-----------------------------------------------------
Floats are numbers with a decimal point.
Example: 3.14, -0.5, 99.99
"""

# TODO: Create a variable called 'price' and assign it a decimal number


# TODO: Print the type of the 'price' variable using type()



"""
-----------------------------------------------------
SECTION 4: STRING (str)
-----------------------------------------------------
Strings are text, written inside single ' ' or double " " quotes.
Example: "Hello", 'Python'
"""

# TODO: Create a variable called 'greeting' and assign it a text message


# TODO: Print the type of the 'greeting' variable using type()



"""
-----------------------------------------------------
SECTION 5: BOOLEAN (bool)
-----------------------------------------------------
Booleans can only have two values: True or False.
They are mostly used for conditions/comparisons.
"""

# TODO: Create a variable called 'is_student' and set it to True or False


# TODO: Print the type of the 'is_student' variable using type()



"""
-----------------------------------------------------
SECTION 6: CHECKING DATA TYPES
-----------------------------------------------------
NOTE: The YouTube video shared with you does NOT cover
this topic in detail. Please check the blog post for a
more detailed video and explanation on Type Checking:
🔗 [https://hariomlohardev.vercel.app/blog/p/python-basics-variables-data-types/]

Python has a built-in function type() which tells you
the data type of any variable.

Example:
x = 10
print(type(x))   # Output: <class 'int'>
"""

# TODO: Create ANY 4 variables (one of each type: int, float, str, bool)
# and print their types one by one



"""
-----------------------------------------------------
SECTION 7: TYPE CONVERSION (CASTING)
-----------------------------------------------------
For a more detailed explanation and video on Type
Conversion, check out the blog post here:
🔗 [https://hariomlohardev.vercel.app/blog/p/python-basics-variables-data-types/]

Sometimes the data you have is in one type, but you need
it in another type to actually use it properly. Converting
one data type into another like this is called
Type Conversion (also known as Casting).

Why does this matter?
Example: If you take a number from the user using input(),
Python stores it as a STRING (text), even if the user typed
"25". So if you try to do math on it directly, like adding
5 to it, Python will give you an ERROR — because you can't
add a number to text. To fix this, you must first CONVERT
that string into an integer or float.

Common conversion functions:
int()   -> converts a value into an integer      Example: int("5")    -> 5
float() -> converts a value into a float          Example: float("5")  -> 5.0
str()   -> converts a value into a string (text)  Example: str(5)      -> "5"
bool()  -> converts a value into a boolean        Example: bool(1)     -> True

Example:
num_str = "5"            # this is a string, not a number
num_int = int(num_str)   # now num_int is 5 (an actual integer)
print(num_int + 10)      # Output: 15 (this works now!)
"""

# TODO: Create a variable 'age_str' with a number stored as a STRING
#       Example: age_str = "18"


# TODO: Convert 'age_str' into an integer and store it in 'age_int'


# TODO: Print the type of 'age_int' to confirm the conversion worked



"""
-----------------------------------------------------
SECTION 8: TAKING USER INPUT
-----------------------------------------------------
NOTE: The YouTube video shared with you does NOT cover
this topic. Please check the blog post for a detailed
video and explanation on how input() works:
🔗 [https://hariomlohardev.vercel.app/blog/p/python-basics-variables-data-types/]

The input() function is used to take input from the user.
NOTE: input() always returns a STRING, even if the user
types a number!

Example:
user_name = input("Enter your name: ")
"""

# TODO: Ask the user to enter their favourite number using input()
#       Store it in a variable called 'fav_number'


# TODO: Print the type of 'fav_number' (it should be a string!)


# TODO: Now convert 'fav_number' into an integer using int()
#       and print its type again (it should now be an integer)



"""
-----------------------------------------------------
SECTION 9: WORKING WITH VARIABLES (Mini Practice)
-----------------------------------------------------
Let's combine everything you've learned so far.
"""

# TODO: Create three variables: 'length', 'width' (both integers or floats)
#       representing the length and width of a rectangle


# TODO: Calculate the area (length * width) and store it in a variable
#       called 'area'


# TODO: Print a message using the variables, for example:
#       "The area of the rectangle is 50"
#       (Use f-strings! Example: print(f"The area is {area}"))



"""
-----------------------------------------------------
SECTION 10: SELF-CHECK QUESTIONS (Answer as comments)
-----------------------------------------------------
Answer the following questions below each one, using a
# comment. This is just for your own understanding, no
need to run code for this section.
"""

# Q1. What is the difference between int and float?
# Your answer:

# Q2. Can a variable's data type change during a program? Why?
# Your answer:

# Q3. What data type does input() always return by default?
# Your answer:

# Q4. What will type(True) return in Python?
# Your answer:


"""
=====================================================
END OF FILE

If you were able to complete all the sections above
without looking anything up, congratulations! You have
understood Variables and Data Types. 🎉

If you struggled anywhere, revisit that section in the
blog post / video, and feel free to ask in the group.
=====================================================
"""
