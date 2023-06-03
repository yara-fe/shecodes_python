# Question 1: 
# Sara is a confident rock climber, but sometimes she forgets her helmet. Rei refuses to climb with Sara unless she's wearing a helmet, because that's Just Sensible.
# Write a program that sets the value for a boolean variable called sara_has_helmet, and then prints out a string indicating whether or not Rei is down to climb.

# sara_has_helmet = True
# print(sara_has_helmet)

# if sara_has_helmet == True:
#     print("Let's send it!")
# else:
#     print("No way, my brain is my moneymaker!")

# Question 2:
# Rei is a very careful climber, but sometimes she is forgetful. Even if Sara has a helmet,they still can't go climbing unless Rei remembers to bring her rope. Add a code to check for the rope before you output the result.

# sara_has_helmet = input("Does Sara has a helmet? True/False: ")
# print(sara_has_helmet)

# sara_has_helmet = True
# rei_has_rope = False

# if sara_has_helmet and rei_has_rope:
#      print("Let's send it!")
# elif not sara_has_helmet and rei_has_rope:
#      print("No way, my brain is my moneymaker!")
# elif sara_has_helmet and not rei_has_rope:
#      print("Who's unprepared now, Rei??")
# elif not (sara_has_helmet and rei_has_rope):
#      print("I guess let's just go hiking?")

# Question 3:
# Write a program that implements the algorithm for red light cameras. The programshould print the string "Flash!" if (and only if) a car is detected driving while the lightis red. If the light is green or amber, the program should print "Do nothing.", even when a car is detected.

# light_color = "Red"
# car_detected = True

# if light_color == "Red" and car_detected:
#     print("Flash!")
# else:
#     print("Do Nothing.")

#Question 4:
# Write a program that asks the user for their height, and determines whether or notthey are tall enough to ride the rollercoaster, which has a height requirement of120cms.

# height = int(input("What is your height in cm?: "))
# # height_int = int(height)

# if height >= 120:
#     print ("Hop on!")
# else:
#     print ("Sorry, not today.")

# Question 5:
# Write a program that asks the user to enter their username and password and output a success message if they are correct, or a failure message if they are incorrect. Your program has one user, whose username is "lucyg", and whose password is "quartzgleam?1"

# define the expected username and password
# username = "lucyg"
# password = "quartzgleam?1"

# # ask users for their username and password
# username_input = input("Enter username: ")
# password_input = input("Enter password: ")

# if username == username_input and password == password_input:
#     print ("Logged in successfully.")
# else:
#     print ("Access denied.")

#Question 6:
# Write a program that asks the user to enter their email address and checks whether it is valid or not. For the purpose of this exercise, you can make the assumption that an email address is valid if it contains a “@” symbol and a “.” symbol


# email = input ("What is your email address?: ")

# if ("@" and ".") in email:
#     print ("Valid email address")
# else: 
#     print ("Invalid email detected!")

# Question 7:
# Will this script print anything to the terminal? Have a think first, decide on youranswer, and then try running it to see if your intuition was correct.If you get a different result to what you thought, see if you can come up with an explanation, and then check with a mentor.

if "False":
    print("A strange game. The only winning move is not to play.")