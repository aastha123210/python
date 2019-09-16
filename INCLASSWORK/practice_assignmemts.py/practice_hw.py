stockSymbol = "MCD"
price = 220.03
change = 0.58
print ("Symbol: " + stockSymbol.upper() + ", Price: " + str(price) + ", Change: " + str(change))
print()
print ("Symbol: " + stockSymbol.lower() + ", Price: " + str(price) + ", Change: " + str(change))
print()
print ("Symbol: " + stockSymbol.upper() + " --- Yesterday's Price: " + str(round(price + change,2)))