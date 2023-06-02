# Takes two numbers from the user and outputs their sum as a float.
# num_one = input ("Enter a number: ")
# num_two = input ("Enter another number: ")
# print(float(num_one)+float(num_two))

# Takes two numbers from the user and outputs the equation representing the multiplication of the two numbers
# num_one = input ("Enter a number: ")
# num_two = input ("Enter another number: ")
# print(f"{float(num_one)} * {float(num_two)} = {float(num_one)*float(num_two)}")

# Takes a distance in kilometers from the user, and output the distance in meters and centimeters.
# distance = input ("How many kilometres? ")
# print(f"{float(distance)}km = {int(distance)*1000}m")

# Takes a distance in kilometers from the user, and output the distance in meters and centimeters.
# distance = input ("How many kilometres? ")
# print(f"{float(distance)}km = {int(distance)*1000}m")

# Takes a distance in kilometers as a float from the user, and output the distance in meters and centimeters.
distance = float(input ("How many kilometres? "))
distance_m = (distance)*10000
distance_cm = distance*100000
print(f"{(distance)}km = {int(distance_m)}m")
print(f"{(distance)}km = {int(distance_cm)}cm")
