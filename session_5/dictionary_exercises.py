# QUESTION 1
# Write a program that asks the user how many of each item they would like in turn, and outputs the total cost of their groceries

# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Coffee": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08
#     }

# for key, value in groceries.items():
#     quantity = input(f"Enter quantity for {key}: ")
#     # quantity = int(quantity)
#     cost = float(quantity) * value
#     print (f"Total cost for {quantity} x {key} is {cost}")

# # QUESTION 2

# colour_counts = {
#     "blue": 0,
#     "green": 0,
#     "yellow": 0,
#     "red": 0,
#     "purple": 0,
#     "orange": 0,
#     }

# QUESTION 3

# import csv

# # Using a context manager to open the file
# with open("shecodes_python\session_5\colours_20_simple.csv", encoding="utf-8") as colour_data:

#     # creating a csv.reader object to grab the data    
#     reader = csv.reader(colour_data)
    
#     #create an empty dictionary
#     colours = {}
    
#     print (colours)

#     # loop time!
#     # for each row in the colours csv file, add the hex and the english name into a dictionary
#     for colour_line in reader:
#        RGB = colour_line[0]
#        hex = colour_line[1]
#        english = colour_line[2]
#        colours[hex] = english

# #print the new dictionary
# print (colours)

# QUESTION 4
# Modify your code from the previous exercise to save both the English name and RGBcode in a list as the value for the corresponding hex code
#"#BEBD7F": ['190-189-127', 'Green beige']
# import csv
# # # Using a context manager to open the file
# with open("shecodes_python\session_5\colours_20_simple.csv", encoding="utf-8") as colour_data:

# # creating a csv.reader object to grab the data    
#     reader = csv.reader(colour_data)

#     #create an empty dictionary and empty list
#     colours_dict = {}
#     rgb_eng_list = []

#     # loop time!
#     # for each row in the colours csv file, add the hex and the english name into a list
#     for colour_line in reader:
#        hex = colour_line[1]
#        rgb_eng = colour_line[0:3:2]
#        colours_dict[hex] =rgb_eng

# #print the new dictionary
# print (colours_dict)

# QUESTION 5

"""
{"#BEBD7F": {"RGB": "190-189-127", "English": "Green beige"}    ...
"""
import csv
# # Using a context manager to open the file
with open("shecodes_python\session_5\colours_20_simple.csv", encoding="utf-8") as colour_data:

# creating a csv.reader object to grab the data    
    reader = csv.reader(colour_data)

    #create an empty dictionary and empty list
    colours_dict = {}
    # dict_2 = {"RGB":[],"English":[]}
    dict_2 = {}

    # loop time!
    # for each row in the colours csv file, add the hex and the english name into a list
    for rgb, hex, eng in reader:
        dict_2["RGB"] = rgb
        dict_2["English"] = eng
    print(dict_2)
#print the new dictionary
# print (colours_dict)

