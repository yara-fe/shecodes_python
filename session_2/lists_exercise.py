#Question 1
## foods = [
#     "orange",
#     "apple",
#     "banana",
#     "strawberry",
#     "grape",
#     "blueberry",    
#     ["carrot", "cauliflower", "pumpkin"],"passionfruit",
#     "mango",
#     "kiwifruit"
## ]

#Print the:
# The first item in the list.
# The third item in the list.
# The last item in the list.
# The first three items in the list.
# The last three items in the list.
# The last item in the sublist

## print(foods[0])
## print(foods[2])
## print(foods[-1])
## print(foods[0:3])
## print(foods[7:])
## print(foods[6][2])

#Question 2:
## lyrics = [    
#     ["Monica", "in my life"],
#     ["Erica", "by my side"],
#     ["Rita's", "all I need"],
#     ["Tina's", "what I see"],    
#     ["Sandra", "in the sun"],    
#     ["Mary", "having fun"],    
#     ["Jessica", "here I am"]
## ]

# print("A little bit of ", lyrics[0][0], lyrics[0][1])

#get the length of the lost
# length = len(lyrics)
# print (i)
#iterate over the index
# for i in range(length):
#     print("A little bit of ", lyrics[i][0], lyrics[i][1]) 

#iterate over each item from the nested list and get the first and second element.
## for item in lyrics:
##     print ("A little bit of", item[0], item[1],";")

#print the rest of the lyrics
## print ("A little bit of you makes me your man (ah!)")  
## print ("*trumpet solo*") 

# #Question 3:
# #Ask user for 3 names. Add each name to a list and then print the list

# #Ask for user input
# name1 = input("Type a name: ")
# name2 = input("Type another name: ")
# name3 = input("Type another name: ")

# #Create an empty list that will store user input.
# namelist = []

# #Put each user input into the empty list (i.e. namelist).
# namelist.append(name1)
# namelist.append(name2)
# namelist.append(name3)

# #print the new namelist.
# print(namelist)

#Question 4
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

#for the first list, use the empty list 'd' to store future values
#Add elements to the blank list by using .append method
d.append(a)
d.append(b)
d.append(c)

#print the new 'd' list
print (d)

#for the second list, use the empty list 'e' to store future values
print (a+b+c)

#Another option is to use .extend method
e.extend(a)
e.extend(b)
e.extend(c)

print (e)
#The .extend method concatenates the first list with another list.
#In comparison, the .append method will add a single element to the end of the list.
#Show difference in results:
print ("Difference between append and extend:")
print (".append method:", (d))
print (".extend method:", (e))
