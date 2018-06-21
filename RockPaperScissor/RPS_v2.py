# Rock Paper Scissor Game
print("Rock..")
print("Paper..")
print("Scissor..")

# Input From two player
player1 = input("player1,make your move: ")
print("**No Cheating!!\n\n" * 20)
player2 = input("player2,make your move: ")

# Nested Conditions to win
if player1 == player2:
    print("Game Tie!")
elif player1 == "Rock":
    if player2 == "Paper":
        print("player2 wins")
    elif player2 == "Scissor":
        print("player1 wins!")
elif player1 == "Paper":
    if player2 == "Rock":
        print("player1 wins!")
    elif player2 == "Scissor":
        print("player2 wins!")
elif player1 == "Scissor":
    if player2 == "Paper":
        print("player1 wins!")
    elif player2 == "Rock":
        print("player2 wins!")
# If Wrong Input is given
else:
    print("Something Wrong!")
