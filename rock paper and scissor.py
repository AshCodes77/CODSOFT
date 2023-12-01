import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!", 1
    else:
        return "Computer wins!", -1

def get_user_choice():
    while True:
        print("\nChoose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_input = input("Enter the number of your choice: ")

        if user_input in ["1", "2", "3"]:
            choices = ["rock", "paper", "scissors"]
            return choices[int(user_input) - 1]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Initialize scores
user_score = 0
computer_score = 0

# Main game loop
while True:
    # Get user and computer choices
    user_choice = get_user_choice()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Display choices
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    # Determine and display the winner
    result, score_change = determine_winner(user_choice, computer_choice)
    print(result)

    # Update scores
    user_score += score_change
    computer_score -= score_change

    # Display scores
    print(f"\nYour Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing rack paper and scissor! Final Scores:")
        print(f"Your Score: {user_score}")
        print(f"Computer Score: {computer_score}")
        break
