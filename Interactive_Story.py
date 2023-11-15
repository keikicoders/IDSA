input("Pick a title: ")

# Define variables
animal = input("Name a animal: ")
action = "waddled"
place = "market"
item = "honey"
reaction = "giggles"

print("\n")

# Construct the story
story = (
    f'''There once was a {animal} who {action} to the {place}.
Looking for some {item} to buy,
but instead of the {item}, she found a guitar,
And played a tune that made everyone respond with {reaction}.
Who knew that a {animal} with a guitar,
Could turn the {place} into a jolly bar!''')

# Print story
print(story)