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

donut_order = ''

print("Welcome to the snack shack!")

while True:
    donut_order = input("What type of donuts would you like?\n-Sprinkles Donuts\n-Chocolate Donuts\n-Plain Donuts\n>")
    if donut_order.lower() == "sprinkles" or donut_order.lower() == "chocolate" or donut_order.lower() == "plain":
        break
    else:
        print("I'm sorry please try again!")


while True:
    donut_count = input("How many donuts would you like to order?\n>")
    if not donut_count.isdigit():
        print("I'm sorry, please enter a valid number")
    else:
        donut_count = int(donut_count)
        if donut_count >= 12:
            donut_count += 1
        break

input("\n\nPress enter to receive your donuts!")

if donut_order.lower() == "sprinkles":
    print(sprinkles_donut * donut_count)
elif donut_order.lower() == "chocolate":
    print(chocolate_donut * donut_count)
elif donut_order.lower() == "plain":
    print(plain_donut * donut_count)
