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

# Ask user for order
print ( '''Welcome to Donuts 'R' Us! Here's our menu:
 - sprinkles donuts
 - chocolate donuts
 - plain donuts
 ''' )
donut_order = input ( "What kind of donuts do you want? " )
number_ordered = input ( "How many donuts do you want to order? " )
number_ordered = int ( number_ordered )
print()

# Add bonus item for large order
if number_ordered >= 12 :
  number_ordered += 1
print ( "Customers who order 12 or more get an extra donut for free!" )
print ( )

# Print order
input ( "Press enter to receive your fresh donuts!" )
if donut_order == "sprinkles" :
  print(sprinkles_donut * number_ordered)
elif donut_order == "chocolate" :
  print (chocolate_donut * number_ordered)
else:
  print(plain_donut * number_ordered)

print ( f"Here's your order of { number_ordered } donuts. Enjoy!")
