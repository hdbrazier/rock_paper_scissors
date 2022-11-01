"""
The computer should randomly choose it's decision 
based on a list of actions it can take ("Rock", "Paper" or "Scissors"). 
The player should then have a chance to input their decision. 
If player and computer choose the same decision then display ("Game Tied"), 
If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), 
if the player chooses "Scissors" and the computer chooses "Rock" display ("You Lose") 
and if the player chooses "Paper" and the computer chooses "Scissors" then display 
("You lose") -- Vice versa for other descisions.
Continue to ask the player for their input until they say "I quit", at which time 
the game will then end and display ("Thank you for playing").
"""
import random

while True:
    player = input("\nEnter a choice (rock, paper, scissors): ")
    actions = ["rock", "paper", "scissors"]
    computer = random.choice(actions)
    print(f"\nYou chose {player}, computer chose {computer}.\n")

    if player == computer:
        print(f"Both players selected {player}. It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose! Paper covers rock!")
        else:
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("You lose! Rock smashes scissors!")
        else:
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("You lose! Scissors cut paper!")
        else:
            print("You lose!")

    play_again = input("\nDo you want to play again? Enter Y or I Quit: \n")
    if play_again.lower() == "i quit":
        print("Thank you for playing!")
        break
