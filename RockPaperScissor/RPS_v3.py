# Rock Paper Scissor Game with Computer
# Importing Randint from random
from random import randint

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
    elif player2 == "scissor":
        print("player wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("player wins!")
    elif player2 == "scissor":
        print("Computer wins!")
elif player1 == "scissor":
    if player2 == "paper":
        print("player wins!")
    elif player2 == "rock":
        print("Computer wins!")
# If Wrong Input is given
else:
    print("Please enter a valid move!")
