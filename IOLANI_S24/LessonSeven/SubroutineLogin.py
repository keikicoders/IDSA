def login():
  while True:
    uInput = input("What is your username?:")
    pInput = input("What is your password?:")
    if uInput == "stephen" and pInput == "cho":
      print("Success")
      break
    else:
      print("I don't recognize that username or password")
      continue
login()
    
