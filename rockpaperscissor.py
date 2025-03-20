import tkinter as tk
import random

def get_computer_choice():
    """Returns a random choice (rock, paper, or scissors) for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the game."""
    if user_choice == computer_choice:
        return "Tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    """Plays the game and updates the GUI."""
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")

# Create and place widgets
rock_button = tk.Button(window, text="Rock", command=lambda: play_game("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", command=lambda: play_game("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()


