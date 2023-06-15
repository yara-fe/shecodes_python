############################################
# USING EXTERNAL INPUT AND OUTPUT FILES
###########################################
##open (file="dogs_are_awesome.csv", mode="r", encoding="utf-8")
# is similar to
##open (file="dogs_are_awesome.csv")
# because by default, the argument is mode set to r and encoding is set to utf-8

##with open (file="dogs_are_awesome.csv", mode="r", encoding="utf-8") as my_file:
##    print(my_file)
#this will error if you run the ide because it will return to the root folder. 
# You will need to cd to your specific folder

#import module
import csv

# with open (file="dogs_are_awesome.csv", mode="r", encoding="utf-8") as my_file:
#     csv_reader = csv.reader(my_file)
#     for row in csv_reader:
#         print(row)
#This will create a list for each row
#You can change the delimeter by setting the parameter value in the argument


#write a file
with open (file="hello.csv", mode="w", encoding="utf-8") as my_file:
    csv_writer = csv.writer(my_file)
    csv_writer.writerow("Hello")