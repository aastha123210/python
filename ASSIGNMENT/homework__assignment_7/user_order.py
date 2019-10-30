#Name:Aastha Giri
#Student ID:0957366
#Due Date: October 29th, 2019
#MSITM 6341

menu_items = {

    "Bacon Guacomole": 9.00,

    "Baja Fish Tacos": 11.00,

    "Seafood Enchiladas": 20.00,

    "Grilled Tilapia": 24.00,

    "Dumplings": 7.00,

    "Cajetas": 15.99

}
customer_order = []
active = True
prompt = "\nPlease enter an item you want to order:"
prompt += "\n(Enter 'done' when you are finished.) "

while active:
    input_order = input(prompt)
    if input_order.lower() == 'done':
        active = False
    else: customer_order.append(input_order)
Total=0
print("\nBelow is your order details:")
for item in customer_order:
    if item in menu_items:
        print('{} : ${}'.format(item,menu_items[item]))
        Total += menu_items[item]
    else:
        print("sorry, we don't have {}".format(item))
print("----------------")
print("Total : $" + str(round(Total,2)))
