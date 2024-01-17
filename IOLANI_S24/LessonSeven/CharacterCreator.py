import time, random
username = 'NOTHING'
password = ''

def register():
    username = input("Create a username: ")
    password = input("Create a password: ")

def login():
  while True:
    uInput = input("What is your username?:")
    pInput = input("What is your password?:")
    if uInput == username and pInput == password:
      print("Success")
      break
    else:
      print("I don't recognize that username or password. Try again")
def rollDice(side):
  result = random.randint(1,side)
  return result

def health_roll ():
  health = (rollDice(6) * rollDice(12))/2+10
  return health

def attack_roll():
  attack = (rollDice(6) * rollDice(8))/2+12
  return attack

while True:
  menu = int(input('Welcome to the Legend Builder! Please \n\n Press 1 to Login \n Press 2 to create a new account\n\n >>'))
  if menu == 1:
    login()
  elif menu == 2:
    register()
    login()
  else:
    print("Please submit valid response")
    continue


  build = int(input('Welcome to the Legend Builder! Please \n\n Press 1 to build a new warrior \n Press 2 to exit\n\n >> '))
  if build ==1:
    name = input('What is the name of your legend? >> ')
    type = input('Human, elf, wizard, or orc >> ')
    print(name)
    print("HEALTH:", health_roll())
    time.sleep(2)
    print("ATTACK:", attack_roll())
    time.sleep(3)
    print('\n\n\n')
  elif build == 2:
    exit()
  else:
    print('Try again\n')
