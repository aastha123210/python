# Name: Aastha Giri
# Student ID: 0957366
# Due Date: 10/1/2019
# MSITM 6341
#
#
######################## Instructions ############################
#
# 1. Resolve any compiler errors
# 2. Follow any instructions given in comments starting with TODO
# 3. Resolve any runtime errors
# 4. Resolve any logical errors until the program outputs EXACTLY as the sample output below shows
#
##################### Program Description ########################
#
# The following program takes the stock prices for the past 6 days
# for a single company. It calculates the change in price over the
# provided days and outputs this change in price and indicates if the stock
# increased, decreased, or stayed the same. 
#
############## Sample Output of Functioning Program ##############
#
# ------------ SBUX ------------
# Yesterday:  Stock Decreased: -0.43
# 2 Days Ago: Stock Increased: 0.89
# 3 Days Ago: Stock Decreased: -0.74
# 4 Days Ago: Stock Increased: 1.49
# 5 Days Ago: No Change in Price
#
##################################################################

########## DO NOT MODIFY ##########
stock_symbol = "sbux"
stock_prices = [90.35, 89.92, 90.81, 90.07, 91.56, 91.56]
###################################

#stock_price_changes = 0

#TODO Write a for loop that iterates over all of the stock prices and computes the change in prices.
#Hint: How many elements should there be in stock_price_changes?


print("------------ " + stock_symbol + " ------------")

idx = 0
#Finding the day for stock prices
for idx in range(0,len(stock_prices)):

    what_day = ""
    if idx == 0:
        what_day = "Yesterday: "
        #print(stock_prices_change)
    else:
        what_day = str(idx + 1) +" Days Ago:"
        
#Calculating the difference on stock prices
    stock_prices_change = round((stock_prices[idx+1]-stock_prices[idx]),2)

    if stock_prices_change < 0:
        print(what_day," Stock Decreased: "+str(stock_prices_change))
    elif stock_prices_change > 0:
        print(what_day, " Stock Increased: "+str(stock_prices_change))
    else:
        print(what_day + " No Change in Price")

    idx = idx + 1