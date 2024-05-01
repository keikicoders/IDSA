# Define the questions, options, and correct answers
question1 = "What is the capital of France?"
options1 = "A) Berlin, B) Madrid, C) Paris, D) Rome"
answer1 = "C"

question2 = "Which planet is known as the Red Planet?"
options2 = "A) Earth, B) Mars, C) Jupiter, D) Venus"
answer2 = "B"

question3 = "Who wrote 'To Kill a Mockingbird'?"
options3 = "A) Harper Lee, B) J.K. Rowling, C) Ernest Hemingway, D) Mark Twain"
answer3 = "A"

# Initialize a score variable to keep track of correct answers
score = 0

# Ask the first question
print("Question 1:", question1)
print("Options:", options1)
user_answer = input(">")

if user_answer == answer1:
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was:", answer1)

print()  # Newline for separation

# Ask the second question
print("Question 2:", question2)
print("Options:", options2)
user_answer = input(">")

if user_answer == answer2:
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was:", answer2)

print()  # Newline for separation

# Ask the third question
print("Question 3:", question3)
print("Options:", options3)
user_answer = input(">")

if user_answer == answer3:
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer was:", answer3)

print()  # Newline for separation

# Display the user's final score
print(f"Your final score is: {score} out of 3")
