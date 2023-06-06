#Select a number, and save it as a variable in your code. 
#Ask the user to enter anumber, and then output whether their number is less than or greater than the selected number. 
#Keep asking until the user guesses the correct number. 
#Then print a congratulatatory message

import random

replay = "yes"

while replay != "no":
    
    # Print title of the game
    print ("Guess the random number!")

    # Generate a random number to be guessed
    answer = random.randint(0,10)

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

    #ask if user wants to play again
    replay = input("If you would like to stop playing, type no. Otherwise, the game will restart. ")

#if user types no, end game and print end message
print ("Thanks for playing!")   
