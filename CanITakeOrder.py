# Initialize variables
total = 0
tax = 0.07  # Sales tax rate of 7%
 
# Generate random prices for each food item
price1 = 5.39
price2 = 6.25
price3 = 7.52
price4 = 2.53
 
# Get food orders and quantities
food1 = "Burgers"
quantity1 = int(input("Enter the quantity of " + food1 + ": "))
 
food2 = "Fish"
quantity2 = int(input("Enter the quantity of " + food2 + ": "))
 
food3 = "Steak"
quantity3 = int(input("Enter the quantity of " + food3 + ": "))
 
food4 = "Fries"
quantity4 = int(input("Enter the quantity of " + food4 + ": "))
 
# Calculate subtotal
subtotal = (quantity1 * price1) + (quantity2 * price2) + (quantity3 * price3) + (quantity4 * price4)
 
# Calculate sales tax
tax = round(subtotal * tax, 2)
 
# Calculate total
total = round(subtotal + tax, 2)
 
# Print receipt
print("\n\nReceipt")
print("----------------------------------------------")
print("Item\t\tQuantity\t\tPrice")
print(food1 + "\t\t" + str(quantity1) + "\t\t\t\t$" + str(price1))
print(food2 + "\t\t" + str(quantity2) + "\t\t\t\t$" + str(price2))
print(food3 + "\t\t" + str(quantity3) + "\t\t\t\t$" + str(price3))
print(food4 + "\t\t" + str(quantity4) + "\t\t\t\t$" + str(price4))
print("\nSubtotal:\t\t$" + str(subtotal))
print("Sales Tax:\t\t$" + str(tax))
print("\nTotal:\t\t\t$" + str(total))
print("----------------------------------------------")