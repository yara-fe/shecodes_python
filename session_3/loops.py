######################
# LOOPS
######################

# Fundamental of good code = DRY = Don't Repeat Yourself

# Loop statement lets us define a block of code that will be executed multiple times. 
# Iterating is the process of doing something multiple times
# Each "turn" or repitition is an iteration

######################
# WHILE
######################
# Execute a chunk of code repeatedly, for as long as some Boolean expression is True.

# While loop syntax:
# while <condition>:
#    <loop body>
# condition is a boolean expression that equates to True or False
# indentation is important!
# condition will be evaluated first.
# If True, python will execute the loop body

# Example:
# Use a while loop to keep adding to a count until it reaches 5.

## count = 0
## while count < 5:
##    count = count + 1 # Add to the previous count number
##    print (count) # Print the new count number

#Code that will run forever:
## while True:
    # Do stuff

#Code that will not be executed if Boolean never evaluates to True:
## while False:
    # Doesn't matter what I put here... it will never run

######################
# FOR
######################

# a statement that will execute it's block of code a limited amount of times
# before executing a code block, we already know how many iterations we will do
# it allows us to iterate a code block over a sequence

# For loop syntax:
# for <counter> in <sequence>:
#   codeblock

# range() function = generates a sequence of integers in memory (doesn't print)
# example: range(10) = [0,1,2,3,4,5,6,7,8,9]
# range(num_1, num_2) = range containing numbers from num_1 up to (but not including) num_2
# range(num_1, num_2, num_3) = range containing every second number from num_1 up to num_2
# Remember that the range() only creates the sequence in memory. If you want to see the numbers in the range, you'll need to convert it to a list.
# Example:
# Create a range: 
## my_range = range(0,21)
# Conver the range to a list:
## my_list = list(my_range)

######################
# NESTED LOOPS
######################

#You can put one loop into another
#Remember python executes the code inside its code block until it has satisfied the conditions we gave it. 