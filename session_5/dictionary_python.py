student_phonebook = {
    "Cindy":111,
    "Jess":222,
    "Yara":333
}

#print the student_phonebook with the 3 students
print(student_phonebook)

#assign a new key and value
student_phonebook["Trace"] = 444

#print the student_phonebook. You should now see the 4 students
print(student_phonebook)

#add a value with an empty key
# student_phonebook["Asli"] = 

#delete 
del student_phonebook["Trace"]

#print the student_phonebook with the 3 students
print(student_phonebook)

#print a value that does not exist
##print(student_phonebook["Asli"])
# This will result in ---> KeyError: 'Asli'


#this will print eack key and value as a string
for key in student_phonebook:
    print(key, student_phonebook[key])

for value in student_phonebook.values():
    print(value)

#Tuple is a data type that can hold more than one values

#Unpacking: 
## a,b = [1,2]
## print(a) #This will result in 1
## print (b) #This will result in 2


#unpacking via the items method
##for key, value in student_phonebook.items():
##    print(key, value)

#Trying to unpack a 3 element list but you only have 2 variables
a,b = [1,2,3]
# This will result in --> ValueError: too many values to unpack (expected 2)