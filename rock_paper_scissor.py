
import random

# List of valid choices
cards = ['rock', 'paper', 'scissor']

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        return "You win!" # \ this symbol is used to split a line into multipe lines for better readability.
    else:
        return "Computer wins!"


def play_game():
    user_count = 0
    computer_count = 0

    for _ in range(5):  # Play 5 rounds
        # Get user input
        user_input = input("Enter Your Choice: ").lower()
        while user_input not in cards:
            print("Invalid choice! Please choose from 'rock', 'paper', or 'scissor'.")
            user_input = input("Enter Your Choice (rock, paper, scissor): ").lower()

        # Get computer's choice
        computer_input = random.choice(cards).lower()

        # Determine the winner of the round
        result = determine_winner(user_input, computer_input)
        print(f"You chose: {user_input}, Computer chose: {computer_input}")
        print(result)

        # Update scores
        if result == "You win!":
            user_count += 1
        elif result == "Computer wins!":
            computer_count += 1

    # Display final results
    print("\nFinal Scores:")
    print(f"You: {user_count}, Computer: {computer_count}")
    if user_count > computer_count:
        print("You are the overall winner!")
    elif computer_count > user_count:
        print("Computer is the overall winner!")
    else:
        print("The match is tie!")

# Run the game
if __name__ == "__main__":
    play_game()