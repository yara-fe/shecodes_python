# Question 1: 
# Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the numbers.

#initate the total value to zero
##total = 0 
##raw_input = input ("Enter a number: ")

#while raw_input is not blank, 
# convert the string input to an integer. 
# add the number to the previous total
# ask for another number
##while raw_input != '':
##    num = int(raw_input)
##    total += num
##    raw_input = input ("Enter a number: ")

# when the raw_input is blank, print the sum
##print ("Your numbers sum to ", total)

# Question 2:
# Ask the user to enter a in integer number. 
# Print all the odd numbers between 0 and that number (inclusive).

# odd number is an integer that is not divisible by 2. 
# Hence in python, we can use the remainder operator % to determine if an integer is odd or even. 
# If a number is divded by 2 and the remainder is 0, it is even.
# If the remainder is not 0, it is odd.


# count = 1
# number = int (input("Enter a number: "))

# while count <= number:
#     if (count % 2 != 0):
#         print(count)
#     count = count + 1

# for number in range (0, number + 1):
#     if number % 2 != 0:
#         print(number, end=" ")

#Question 3:
#Select a number, and save it as a variable in your code. 
#Ask the user to enter anumber, and then output whether their number is less than or greater than the selected number. 
#Keep asking until the user guesses the correct number. 
#Then print a congratulatatory message

# Select the number to be guessed
answer = 10

# Print title of the game
print ("Guess the random number!")

#Ask user to enter a number
guess = int(input("Make a guess: "))

#game logic
while guess != answer:
    if guess < answer:
        print ("Too low...")
    else: 
        print ("Too high...")
    #ask user to make another guess
    guess = int(input("Make a guess: "))

#print congratulatory message if user guesses correctly.
print("You got it right!")