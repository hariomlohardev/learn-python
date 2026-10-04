"""
=====================================================
   PYTHON PRACTICE FILE - ARITHMETIC OPERATORS
=====================================================

Welcome! This file will help you test whether you have
understood Arithmetic Operators in Python.

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
SECTION 1: ADDITION (+)
-----------------------------------------------------
The + operator adds two numbers together.
Example: 5 + 3 -> 8
"""

# TODO: Create two variables 'a' and 'b' with any whole numbers


# TODO: Print the result of adding 'a' and 'b'



"""
-----------------------------------------------------
SECTION 2: SUBTRACTION (-)
-----------------------------------------------------
The - operator subtracts the right number from the left.
Example: 10 - 4 -> 6
"""

# TODO: Create two variables 'x' and 'y' with any whole numbers


# TODO: Print the result of subtracting 'y' from 'x'



"""
-----------------------------------------------------
SECTION 3: MULTIPLICATION (*)
-----------------------------------------------------
The * operator multiplies two numbers.
Example: 4 * 3 -> 12
"""

# TODO: Create two variables 'length' and 'width'


# TODO: Print the result of multiplying 'length' and 'width'



"""
-----------------------------------------------------
SECTION 4: DIVISION (/)
-----------------------------------------------------
The / operator divides the left number by the right number.
It ALWAYS returns a float, even if the result is a whole number.
Example: 10 / 2 -> 5.0
"""

# TODO: Create two variables 'total' and 'people'


# TODO: Print the result of dividing 'total' by 'people'


# TODO: Print the type() of that result (it should be a float!)



"""
-----------------------------------------------------
SECTION 5: FLOOR DIVISION (//)
-----------------------------------------------------
The // operator divides and rounds DOWN to the nearest
whole number (drops anything after the decimal point).
Example: 10 // 3 -> 3
"""

# TODO: Using the same 'total' and 'people' variables from Section 4,
#       print the result of floor dividing 'total' by 'people'



"""
-----------------------------------------------------
SECTION 6: MODULUS (%)
-----------------------------------------------------
The % operator gives you the REMAINDER left over after
division.
Example: 10 % 3 -> 1   (because 3 goes into 10 three times,
                         with 1 left over)
"""

# TODO: Using the same 'total' and 'people' variables from Section 4,
#       print the remainder when 'total' is divided by 'people'


# TODO: Create a variable 'number' and assign it any whole number.
#       Then use % to check if it is EVEN or ODD, and print
#       either "Even" or "Odd" based on the remainder.
#       (Hint: if number % 2 == 0, it is even)



"""
-----------------------------------------------------
SECTION 7: EXPONENTIATION (**)
-----------------------------------------------------
The ** operator raises the left number to the power of
the right number.
Example: 2 ** 3 -> 8   (2 * 2 * 2)
"""

# TODO: Create a variable 'base' and a variable 'power'


# TODO: Print the result of raising 'base' to the power of 'power'



"""
-----------------------------------------------------
SECTION 8: OPERATOR PRECEDENCE (ORDER OF OPERATIONS)
-----------------------------------------------------
Python follows PEMDAS, just like in math class:
Parentheses -> Exponents -> Multiplication/Division -> Addition/Subtraction

Example:
result = 2 + 3 * 4
print(result)   # Output: 14, NOT 20
"""

# TODO: Without running the code yet, write down (as a comment) what
#       YOU think the output of the following line will be:
# expression_1 = 10 + 2 * 5
# Your guess:

# TODO: Now actually create that variable and print it to check
#       if your guess was correct
expression_1 = 10 + 2 * 5



# TODO: Create an expression using parentheses that changes the
#       order, so that the addition happens BEFORE the multiplication.
#       Print the result.



"""
-----------------------------------------------------
SECTION 9: WORKING WITH VARIABLES (Mini Practice)
-----------------------------------------------------
Let's combine everything you've learned in this file.
"""

# TODO: You bought 'quantity' number of items, each costing 'price'.
#       Create both variables with any values you like.


# TODO: Calculate the total cost (quantity * price) and store it
#       in a variable called 'total_cost'


# TODO: You have a budget of 'budget' amount. Create that variable too.


# TODO: Calculate how much money you'll have left after the purchase
#       (budget - total_cost) and store it in 'remaining_balance'


# TODO: Print a message using f-strings showing the total cost and
#       the remaining balance.
#       Example: "Total cost: 50, Remaining balance: 25"



"""
-----------------------------------------------------
SECTION 10: SELF-CHECK QUESTIONS (Answer as comments)
-----------------------------------------------------
Answer the following questions below each one, using a
# comment. This is just for your own understanding, no
need to run code for this section.
"""

# Q1. What is the difference between / and // in Python?
# Your answer:

# Q2. What does the % operator actually give you as a result?
# Your answer:

# Q3. In the expression "2 + 3 * 4", which operation happens first, and why?
# Your answer:

# Q4. How would you use % to check if a number is even or odd?
# Your answer:

# Q5. What data type does the / operator always return?
# Your answer:


"""
-----------------------------------------------------
SECTION 11: STRING METHODS
-----------------------------------------------------
Watch this video first: https://www.youtube.com/watch?v=tb6EYiHtcXU
("String methods in Python are easy! 〰️")

Strings have built-in methods that let you change,
check, or clean up text easily. A method is called using
a dot after the variable, like this:

Example:
text = "hello"
print(text.upper())   # Output: HELLO
"""

# TODO: Create a variable called 'sentence' with any text of your choice


# TODO: Print the UPPERCASE version of 'sentence' using .upper()


# TODO: Print the lowercase version of 'sentence' using .lower()


# TODO: Print the LENGTH of 'sentence' using len()


# TODO: Create a variable called 'messy_text' with extra spaces before
#       and after a word, like "   hello   "
#       Then print it AFTER removing the extra spaces using .strip()


# TODO: Using 'sentence', replace one word in it with another word
#       using .replace("old_word", "new_word") and print the result


# TODO: Check if 'sentence' starts with a specific letter/word using
#       .startswith() and print the result (True or False)



"""
-----------------------------------------------------
SECTION 12: SELF-CHECK QUESTIONS (String Methods)
-----------------------------------------------------
Answer the following questions below each one, using a
# comment.
"""

# Q1. What does .upper() do to a string?
# Your answer:

# Q2. What does .strip() remove from a string?
# Your answer:

# Q3. Does len() count spaces as characters too?
# Your answer:

# Q4. What does .replace() need you to provide as arguments?
# Your answer:


"""
=====================================================
END OF FILE

If you were able to complete all the sections above
without looking anything up, congratulations! You have
understood Arithmetic Operators AND String Methods. 🎉

If you struggled anywhere, revisit that section in the
blog post / video, and feel free to ask in the group.
=====================================================
"""
