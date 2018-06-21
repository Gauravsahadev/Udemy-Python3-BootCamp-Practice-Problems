# Rock Paper Scissor Game with Computer
# Importing Randint from random
from random import randint
# initial computer and player score
computer_wins = 0
player_wins = 0


while (computer_wins < 3) and (player_wins < 3):
    print("Scores: Computer: {} Player: {}".format(computer_wins, player_wins))
    print("Rock..")
    print("Paper..")
    print("Scissor..")
    # Generating random number from 0 to 2
    rand_num = randint(0, 2)

    # Input From computer and player
    player1 = input("player,make your move: ").lower()

    if rand_num == 0:
        player2 = "rock"
    elif rand_num == 1:
        player2 = "paper"
    else:
        player2 = "scissor"
    print("Computer plays {}".format(player2))

    # Nested Conditions to win
    if player1 == player2:
        print("Game Tie!")
    elif player1 == "rock":
        if player2 == "paper":
            print("Computer wins")
            computer_wins += 1
        elif player2 == "scissor":
            print("player wins!")
            player_wins += 1
    elif player1 == "paper":
        if player2 == "rock":
            print("player wins!")
            player_wins += 1
        elif player2 == "scissor":
            print("Computer wins!")
            computer_wins += 1
    elif player1 == "scissor":
        if player2 == "paper":
            print("player wins!")
            player_wins += 1
        elif player2 == "rock":
            print("Computer wins!")
            computer_wins += 1
    # If player wants to quit
    elif player1 == "quit" or "q":
        break
    # If Wrong Input is given
    else:
        print("Please enter a valid move!")

if computer_wins == player_wins:
    print("Its a Tie")
elif computer_wins > player_wins:
    print("Oh NO ! Computer wins :(")
else:
    print("Player wins \U0001f600")
    print(
        "Final Scores: Computer: {} Player: {}".format(
            computer_wins,
            player_wins))
