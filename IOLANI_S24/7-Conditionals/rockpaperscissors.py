import random

computer_score = 0
player_score = 0

while computer_score != 5 and player_score != 5:
    
    moves = ["rock", "paper", "scissors"]
    computer_move = random.choice(moves)
    #use input to get the move from the user    
    player_move = input("What move do you want to perform?")
    print(player_move)
    print(computer_move)
    #use if statement to see who wins
    if player_move == computer_move:
        print("it is a draw!")
    elif player_move == "scissors" and computer_move == "paper":
       print("You win!")
       player_score = player_score + 1
    #rock beats scissors
    elif player_move == "rock" and computer_move == "scissors":
       print("You win!")
       player_score = player_score + 1
    #paper beats rock
    elif player_move == "paper" and computer_move == "rock":
        print("You win!")
        player_score = player_score + 1
    else:
        print("You lost :((( L")
        computer_score = computer_score + 1
    print("computer: " + str(computer_score) + "\nplayer: " + str(player_score))


