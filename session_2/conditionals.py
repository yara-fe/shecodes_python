############
# Other Notes:
###########
# syntax = grammatical error
# semantic = logical error

#############
# INSTRUCTIONS: 
#############
# Code lines with double hash (##) are codes commented out. 
# Uncomment so you can run the code.

############
# Boolean
############
# Takes two values only where one is True and other value is False.

## name = "Yara"
## age = 28
## my_variable = True
## my_variable2 = False

#print the value of my_variable
## print(my_variable)
#Result on terminal: True

#print the type of data for the variable my_variable
## print(type(my_variable))
#Result on terminal: <class 'bool'>

#Boolean expressions - expressions that produce a Booleon value
#Comparison Operators
# == means is equal to
# != means is not equal to
# > means greater than
# < means less than
# >= means greater than or equal to
# <= means less than or equal to

#Example:
## print(5 < 3)
#Result on terminal: False

#Compare two floats
## print (3.5 > 6.3)
#Result on terminal: False

#Python is case sensitive and will differentiate lower and upper cases, so you can compare strings in a Boolean expression:
## print("Asli" == "asli")

#Boolean Operators

# (1) NOT = reverses the value of the variable
## is_sunny = True
## print(not is_sunny)
# Result on terminal: False

# (2) AND = combines two boolean expressions. Both expressions must be true
# is_sunny = True
# is_warm = True
# This will only print a True result if it is both sunny AND warm
## print(is_sunny and is_warm)
# Result on terminal: True

# (3) OR = determines whether either of the expressions is true. 
# is_sunny = True
# is_warm = False
# If at least one expression is true, consequently, the result is true.
## print(is_sunny or is_warm)
# Result on terminal: True
# True or True = True
# True or False = True
# False or True = True
# False or False = False

##############
# CONDITIONALS
##############

# (1) Conditional "if" statement

#declare temperature as a variable and assign an integer value
## temperature = 18

# Write an if function to check if the expression "is the temperature greater than 18?" is true. If it is true, print "Weather is nice!"

#Scenario 1: When the expression is true
## if temperature > 17:
##    print("Weather is nice!")
# Result on terminal: "Weather is nice"

#Scenario 2: When the expression is false
## if temperature > 19:
##    print("Weather is nice!")
# Result on terminal: blank

# (2) Conditional "if-else" statement
# If-else allows you to have a result if the expression is false.

temperature=18

if temperature > 19:
    print("Weather is nice!")
else:
    print("Weather is too cold!")
# The if function above checks the expression "temperature variable is greater than 17"
# If it is true, it will print "Weather is nice!"
# If it is false, it will print "Weather is too cold"
# Result on termina: The above function will print "Weather is too cold" because the expression is false.
