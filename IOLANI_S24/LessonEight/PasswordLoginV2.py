username = "keikicoders"
password = "ilovecoding"
user_input_username = ''
user_input_password = ''

print("Welcome to the best app in the world. In order to enter you must enter your username and passoword")


while True:
  user_input_username = input("Username: ")
  user_input_password = input("Password: ")
  if user_input_username != username and user_input_password != password:
    print("Access denied! Try again")
  else:
    print("Access granted!")
    break
