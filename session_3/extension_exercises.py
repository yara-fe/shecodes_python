#The code below will produce a grocery receipt 
#based on how many units of each item was bought by the user.
#The receipt will also show the total price of the groceries bought

#List of grocery items and their prices per unit
groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["BBQ Shapes", 9.00],
    ["Bread", 2.10],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

#Set an empty list where total price for each grocery item will be saved
price_list = []

#Ask user how many units of each item they bought
for item in groceries:
    question = "Please enter the quantity for " + str(item[0]) + ": "
    quantity = float(input(question))
    #Each item's total price
    price = item[1] * quantity
    #add each item's price to the price_list
    price_list.append(price)

#sum up all the prices in the price_list
grocery_price = 0
for amount in price_list:
    grocery_price = grocery_price + float(amount)

print ("Thank you, your total is $", grocery_price)
