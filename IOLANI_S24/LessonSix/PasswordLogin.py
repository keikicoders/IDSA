username = "keikicoders"
password = "ilovecoding"

print("Welcome to the best app in the world. In order to enter you must enter your username and passoword")
user_input_username = input("Username: ")
user_input_password = input("Password: ")

if user_input_username == username and user_input_password == password:
  print("Access granted!")
else:
  print("Access denied")
