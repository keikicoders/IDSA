# Assign price variables
burger_price = 4.79
donut_price = 4.29
salad_price = 3.99
water_price = 0.99
sales_tax_percent = 8.25

# Get number order for each menu item
print("Welcome to Hello Food, home of the World Burger! May I take your order?")
print()
print("How many World Burgers would you like?")
burger_order = input("> ")
print("How many bacon donuts would you like?")
donut_order = input("> ")
print("How many banana avocado salads would you like?")
salad_order = input("> ")
print("How many bottles of organic water would you like?")
water_order = input("> ")

# Calculate subtotal for each item
# subtotal = price * number ordered
burger_subtotal = burger_price * float(burger_order)
donut_subtotal = donut_price * float(donut_order)
salad_subtotal = salad_price * float(salad_order)
water_subtotal = water_price * float(water_order)

# Round subtotals to dollars and cents
burger_subtotal = round(burger_subtotal, 2)
donut_subtotal = round(donut_subtotal, 2)
salad_subtotal = round(salad_subtotal, 2)
water_subtotal = round(water_subtotal, 2)

# Calculate subtotal for order
# Add subtotals for each item together
subtotal = burger_subtotal + donut_subtotal + salad_subtotal + water_subtotal
subtotal = round(subtotal, 2)

# Calculate sales tax from order subtotal
# Make tax percent into decimal by dividing by 100
# tax amount = tax percentage * order amount
sales_tax = sales_tax_percent / 100 * subtotal
sales_tax = round(sales_tax, 2)

# Calculate order total
# Add order subtotal and sales tax
total_price = subtotal + sales_tax
total_price = round(total_price, 2)

# Create receipt string
receipt = f'''
-----------------------------------------------
 *** Hello Food ***
 7100 Hello World Rd.
 Austin, TX
================================================
Unit Price   Quantity    Description       Price
================================================
{burger_price}          {burger_order}        WRLD BURGER        {burger_subtotal}
{donut_price}           {donut_order}         BACON DONUT        {donut_subtotal}
{salad_price}           {salad_order}         BAN AV SALAD       {salad_subtotal}
{water_price}           {water_order}         ORG WATER          {water_subtotal}

                            ---------------------
                                  Subtotal: ${subtotal}
                           {sales_tax_percent}% Sales Tax: ${sales_tax}

                                     Total: ${total_price}
=================================================
'''

# Print receipt
print()
print(receipt)
