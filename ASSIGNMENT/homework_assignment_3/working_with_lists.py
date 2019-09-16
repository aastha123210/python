grocery_items = ['White Bread', 'Tomatoes', 'Rice', 'Milk', 'Cornflakes']
price_of_grocery_items = [1.30, 2.5, 5.7, 3.75, 4.08]

#printing 3rd item and its price
print(grocery_items[2] + '$' + str(price_of_grocery_items[2]))

#printing the last item and its price
print(grocery_items[-1] + '$' + str(price_of_grocery_items[-1]))

#Adding a 6th item and its price
grocery_items.append('Potatoes')
price_of_grocery_items.append(6.25)
print(grocery_items[5] + '$' + str(price_of_grocery_items[5]))

#printing the list of items 
print(grocery_items)

#printing the list of price
print(price_of_grocery_items)

#Removing the first item and its price 
del grocery_items[0]
del price_of_grocery_items[0]

#Doubling the price of 2nd item 
doube_price = price_of_grocery_items[1]*2
price_of_grocery_items[1] = doube_price

#printing the list of items 
print(grocery_items)

#Printing the list of price
print(price_of_grocery_items)