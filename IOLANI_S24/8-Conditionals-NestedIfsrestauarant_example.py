print("Welcome to our restaurant!")
choice1 = input("Will you be dining with us?\n1. Yes \n2. No\n>")

if choice1 == "Yes":
    choice2 = input("Do you have money?\n1. Yes \n2. No\n>")
    if choice2 == "Yes":
        print("Here is your menu!")
        choice3 = input("Would you like \n1. Tap Water or \n2.Sparkling Water?\n>")
        if choice3 == "Tap Water":
            print("The tap water will be out shortly!")
        else:
            print("Ooh, sparkling water. You are very refined!")
    else:
        print("Sorry you need money to dine here! Goodbye")
else:
    print("Ok! You can leave the restaurant! Goodbye!")
    
    
    
    
