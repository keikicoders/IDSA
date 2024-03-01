# Ask user to input words
animal = input("Name an animal: ")
adjective = input("Name an adjective: ")
clothing = input("Name a piece of clothing: ")
food_1 = input("Name a food: ")
verb_ing = input("Name a verb ending in -ing: ")
food_2 = input("Name another food: ")
number = input("Name a number: ")
job = input("Name a job: ")
instrument = input("Name a musical instrument: ")
song = input("Name a song: ")

# Combine user input with story title
title = f"Breaking News! Wild {animal} causes chaos"

# Combine user input with story
story = f'''A {adjective} {animal} wearing a {clothing} caused chaos on Sunday, stopping traffic on Main Street for hours. The animal ate all of the {food_1} in the grocery store, then ran through the town square. After {verb_ing} in the fountain for {number} minutes, it helped itself to {food_2} left behind by a group of {job}s. As people watched from a distance, the {animal} stopped eating and looked around. Then, without warning, it pulled out a {instrument} and played "{song}" for the crowd.'''

# Output story title
print()
print(title)
print()

# Output story
print(story)
