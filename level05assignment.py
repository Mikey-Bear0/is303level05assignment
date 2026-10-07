### ROCK PAPER SCISSORS

import random

## Welcome user to the game
print("Welcome to RPS (Rock Paper Scissors)")

## Ask how many rounds they'd like to play (must be odd number)
rounds = 0

# If it's not a valid input like an even number or a string, prompt the user again
while True:
    try:
        rounds = int(input("How many rounds would you like to play? (must be an odd number) "))
        if rounds % 2 == 0:
            print("Please enter an odd number for the rounds.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"Great! We will play {rounds} rounds.")

player_score = 0
computer_score = 0
round_count = 1

while rounds > 0:
    
    print(f"Round {round_count}")

    def get_player_choice():
        # Collect and validate the player's choice
        choice = input("Enter rock, paper, or scissors: ")
        # Convert the input to lowercase to handle case-insensitive input
        choice = choice.lower()
        while choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            choice = input("Enter rock, paper, or scissors: ")
            choice = choice.lower()
        return choice

    ## Collect user's choice
    user_choice = get_player_choice()

    ## Have the computer randomly pick an option
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose {computer_choice}")

    ## Determine the winner
    outcome = ""

    # Function that returns "tie", "win", or "loss"
    def determine_winner():
        if user_choice == computer_choice:
            outcome = "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            outcome = "win"
        else:
            outcome = "loss"
        return outcome
    
    outcome = determine_winner()
    if outcome == "tie":
        print("It's a tie! Play again.")
    elif outcome == "win":
        print("You win!")
        player_score += 1
        rounds -= 1
        round_count += 1
    else:
        print("Computer wins!")
        computer_score += 1
        rounds -= 1
        round_count += 1

# Formatting
print("\n")
print("--------------------------")
    
## Determine and print who won the game
print(f"Final Scores - You: {player_score}, Computer: {computer_score}")
if player_score > computer_score:
    print("Congratulations! You won the game!")
elif player_score < computer_score:
    print("Computer won the game! Better luck next time.")
else:
    print("The game ended in a tie!")

print("Thanks for playin'")