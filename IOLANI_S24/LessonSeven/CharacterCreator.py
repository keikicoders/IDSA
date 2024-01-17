import time
import random

#ACCOUNT CHECKER
def register():
    username = input("Create a username: ")
    password = input("Create a password: ")
    print('Thank you for creating your account. You will be prompted to enter your credentials.')
    return username, password

#PASSWORD CHECKER
def login(username, password):
    while True:
        uInput = input("What is your username?:")
        pInput = input("What is your password?:")
        if uInput == username and pInput == password:
            print("Login success")
            break
        else:
            print("I don't recognize that username or password. Try again")

#FUNCTION TO RETURN A RANDOM ROLL. USER INPUTS HOW MANY SIDES THEY WANT ON THE DI
def rollDice(side):
    result = random.randint(1, side)
    return result

#RANDOMLY DETERMINES LEGEND HEALTH. CAN USE ANY EQUATION YOU WANT.
def health_roll():
    health = (rollDice(6) * rollDice(12)) / 2 + 10
    return health
    
#RANDOMLY DETERMINES LEGEND ATTACK. CAN USE WHATEVER EQUATION YOU WANT
def attack_roll():
    attack = (rollDice(6) * rollDice(8)) / 2 + 12
    return attack

while True:
    menu = int(input('Welcome to the Legend Builder! Please \n\n Press 1 to Login \n Press 2 to create a new account\n\n >>'))
    if menu == 1:
        # Assuming you want to store the returned values from register in variables
        username, password = register()
        login(username, password)
    elif menu == 2:
        # Assuming you want to store the returned values from register in variables
        username, password = register()
        login(username, password)
        break
    else:
        print("Please submit a valid response")
        continue

while True:
    build = int(input('Welcome to the Legend Builder! Please \n\n Press 1 to build a new warrior \n Press 2 to exit\n\n >> '))
    if build == 1:
        name = input('What is the name of your legend? >> ')
        char_type = input('Human, elf, wizard, or orc >> ')
        print(name)
        #DETERMINE LEGEND HEALTH
        print("HEALTH:", health_roll())
        time.sleep(2)
        #DETERMINE LEGEND ATTACK
        print("ATTACK:", attack_roll())
        time.sleep(3)
        print('\n\n\n')
    elif build == 2:
        print("Goodbye!")
        break
    else:
        print('Try again\n')
