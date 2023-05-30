# # # # # # #
# VARIABLES
# # # # # # #
# Variable are containers used for storing data. For example:
# Create a variable named first_name and last_name
# first_name = "Yara"
# last_name = "Tuguinay"

# # # # # # # # # # # # # #
# NAMING CONVENTION
# # # # # # # # # # # # # #
# # - Use lower cases and separate with underscore _


# # # # # # #
# DATA TYPES
# # # # # # #
# (1) Text data - string
# Create a variable with a string data and display the variable value onto the terminal. For example:
# today = "Tuesday"
# print(today)
# 
# Formatted string literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.
# print(f"Today is {today}") 
# 

# # (2) Numerical Data -Integer, Float
# # numerical data types do not need quotes
# # Integer = whole number
# dog_age = 4
# print(type(dog_age))
# print(f"Parker is turning {dog_age+1} soon!")
# # Float = decimal
# dog_weight = 5.2
# print(type(dog_weight))
# print(f"Parker target weight is {dog_weight+1}!")

# # Find the data type of a variable
# # type(variable)
# type(today)
# print(type(today))

# distance = "5000"
# print(distance + 8)
# This will result in error as distance is a string data type whilst 8 is an integer

# Change the variable type of distance from string to integer
# int(distance)
# Now retry to print the expression
# print (int(distance)+8)

# Take an input from the user and return it
# input("")
# input("What's your name?") 
# You can then store the data from the input into a variable
# dog_name = input("What's your name: ")
# print(f"Nice to meet you {dog_name}")

# Calculations with input and variables
# Input function stores the data as string
birth_year = input ("What year were you born? ")
print(f"You are {2023-int(birth_year)} years old")