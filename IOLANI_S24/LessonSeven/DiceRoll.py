import random
def rollDice(sides):
  result = random.randint(1,sides)
  return result
def roll_6_and_8():
  roll_6_sided_di = rollDice(6)
  roll_8_sided_di = rollDice(8)
  health = roll_6_sided_di * roll_8_sided_di
  return health
