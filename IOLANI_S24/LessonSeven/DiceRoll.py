import random
def rollDice(sides):
  result = random.randint(1,sides)
  return result
def roll_6_and_8():
  roll_6_sided_di = rollDice(6)
  roll_8_sided_di = rollDice(8)
  health = roll_6_sided_di * roll_8_sided_di
  #could also write health = rollDice(6) * rollDice(8) to simplifiy but it might be easier for them to break it into two parts!
  return health

print(roll_6_and_8()) 
#be sure to show the student wow we output it. Returning 'health' won't  actually show it. It just stores it for later. We need to print it to show it to the user!
