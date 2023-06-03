#########################
# LISTS
##########################

# Lists store multiple data points
# List is an ordered collection of "slots" that can hold values
# Eg. list_name = [] #lists with no values

# Lists can take any data type and can contain multiple data types within one list (even another list!}
# The list below has multiple data types (string, int, float). 
# It has 3 elements. Each element is separated by a comma.
# E.g list_name = ["Yara", 1 ,1.5]

############################
# INDEXING
############################

#To locate an element within a list, we use index.
#Index is the order of the elements within the list.
#Index counting starts with 0.
#E.g: alphabet = ["a","b","c","d"]
# Element a is in index 0, Element b is in index 1, Element c is in index 2 and so on.
# You can use the index of an element to extract its value.
# Example: Extract the 2nd element from the list alphabet.
## alphabet = ["a","b","c","d"]
## print(alphabet[1])
#Result: b

## alphabet = ["a","b","c","d"]
## print(alphabet[-1]) #gives the last element in the list
## print(alphabet[-2]) #gives the 2nd last element
# negative indexing begins the slicing from the end of the string.

#########################
# SLICING
#########################
#Allows you to select specific elements within the list

#Get element in order 0 up to order 3 (i.e. start inclusive; end exclusive)
## alphabet = ["a","b","c","d"]
## print(alphabet[0:3])
#Result: ['a', 'b', 'c']

#Get every element on the list from the order 2 onwards (i.e."c" onwards)
## alphabet = ["a","b","c","d"]
## print(alphabet[2:])
#Result: ['c', 'd']

#Get all the elements from alphabet
## alphabet = ["a","b","c","d"]
## print(alphabet[0:5])
#Result: ['a', 'b', 'c','d']

############################
# SKIPPING ELEMENTS
############################

#Now let's skip every second element in the list
## alphabet = ["a","b","c","d"]
## print(alphabet[0:5:2])
#Result: ['a', 'c']

############################
# ADDING AND REMOVING ELEMENTS
############################

#.APPEND = Adding a value to the end of  list
#Let's add one more letters to our list 
##alphabet = ["a","b","c","d"]
##alphabet.append('e')
##print (alphabet)
#Result: ['a', 'b', 'c', 'd', 'e']
#Find the length of the list

#.POP = removes element from end of list and hang onto the value you removed
##alphabet = ["a","b","c","d"]
##alphabet.pop() 
##print (alphabet)
#Result: ['a', 'b', 'c']

# The element that has been removed from a pop is considered a returned value. 
# Which means it is stored and you can assign a variable to it and reuse it.
##alphabet = ["a","b","c","d"]
##popped_element = alphabet.pop()
##print (popped_element) 
#Result: d #This is the last element that was removed from the list
#Now the new alphabet list will be:
##print(alphabet)
#Result: ['a', 'b', 'c']

############################
# NESTED LIST
############################
#Lists can contain another list
## letters = ["a","b","c","d",["ef","gh"]]
#The inner list is considered one element
#So we can say that the list letters has 5 elements.
## print (letters[4])
#Result: ['ef', 'gh']
#Notice that it resulted in printing the whole inner list. 
#To get the actual element within the inner list, you can drill down.
## print(letters[4][0])
#Result:ef
#The second index refers to the order within the inner list. So it is getting the first element in the inner list.

#To check if an element exists in your list, use an IF statement and IN as the operator:
#Example: Check if letter a is an element of the list letters
## letters = ["a","b","c","d",["ef","gh"]]
## if 'a' in letters:
##     print("It's in the list")
#Result: It's in the list

#Remember python is case sensitive. What if we put "A"?
##letters = ["a","b","c","d",["ef","gh"]]
##if 'A' in letters:
##    print("It's in the list")
#Result: prints nothing on the terminal because "A" is not in the list