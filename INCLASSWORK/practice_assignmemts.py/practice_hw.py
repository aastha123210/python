stockSymbol = "aapl"
price = 204.66
change = -4.08

print ("Symbol: " + stockSymbol.upper() + ", Price: " + str(price) + ", Change: " + str(change))
print()

print ("Symbol: " + stockSymbol.lower() + ", Price: " + str(price) + ", Change: " + str(change))
print()

print ("Symbol: " + stockSymbol.upper() + " --- Yesterday's Price: " + str(round(price + change,2))