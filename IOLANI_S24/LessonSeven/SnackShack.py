sprinkles_donut = '''
        __
    .-"   "-.
  .'◜   ◜    `.
 /   ◜   ◜   ◜ |
| ◜    .-. ◜    |
|  ◜  (   )   ◜ |
|◜  ◜  `-'  ◜   |
 \   ◜   ◜   ◜ /
  `.  ◜    ◜ .'
    `-.___.-'
'''

plain_donut = '''
        __
    .-"   "-.
  .'         `.
 /             |
|      .-.      |
|     (   )     |
|      `-'      |
 \             /
  `.         .'
    `-.___.-'
'''

chocolate_donut = '''
        __
    .-"***"-.
  .'**/******`.
 /**/**********|
|****/*.-.******|
|*****(   )*****|
|*/****`-'******|
 \***/*********/
  `.*********.'
    `-.***.-'
'''

donut_order = input("Welcome to the snack shack! What type of donuts would you like?\n-Sprinkles Donuts\n-Chocolate Donuts\n-Plain Donuts\n>")
donut_count = int(input("How many donuts would you like to order?\n>"))

if donut_count >= 12:
  print("Customers who order 12 or more donuts get one for free!")
  donut_count += 1

input("\n\nPress enter to receive your donuts!")

if donut_order.lower() == "sprinkles":
  print(sprinkles_donut * donut_count)
elif donut_order.lower() == "chocolate":
  print(chocolate_donut * donut_count)
elif donut_order.lower() == "plain":
  print(plain_donut * donut_count)
                    
