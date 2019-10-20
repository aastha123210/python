#Name:Aastha Giri
#Student ID:0957366
#Due Date: October 20th, 2019
#MSITM 6341

menu_items = {

    'Bacon Guacomole': 9.00,

    'Baja Fish Tacos': 11.00,

    'Seafood Enchiladas': 20.00,

    'Grilled Tilapia': 24.00,

    'Dumplings': 7.00,

    'Cajetas' : 15.99

}

ordered_items = {

    'Bacon Guacomole',

    'Nachos',

    'Dumplings'

}

 

total=0

for item in ordered_items:

    if item in menu_items:

      print('{} : ${}'.format(item,menu_items[item]))

      total += menu_items[item]

    else:

      print("We do not have {}".format(item))

print('---------------------')

print('Order Total : ${}'.format(total))