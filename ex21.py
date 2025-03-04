# rock paper scissors game
import random

choices = ["rock", "paper", "scissors"]
is_running = True

print("Welcome to Rock, Paper, Scissors! ✊📄✂️")
print("The computer will choose a random option and you will have to choose between rock, paper, or scissors.")
print("The rules are simple:")
print("✊ Rock beats ✂️ Scissors")
print("✂️ Scissors beats 📄 Paper")
print("📄 Paper beats ✊ Rock")
print("Enter 'q' to quit")

while is_running:
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if user_choice in choices:
        print(f"Computer chose {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie! 🤝")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("You win! ✊ beats ✂️")
            else:
                print("You lose! 📄 beats ✊")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("You win! ✂️ beats 📄")
            else:
                print("You lose! ✊ beats ✂️")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("You win! 📄 beats ✊")
            else:
                print("You lose! ✂️ beats 📄")
    elif user_choice == "q":
        is_running = False
        print("Thanks for playing! Goodbye! 👋")
    else:
        print("Please enter a valid choice (rock, paper, scissors) or 'q' to quit.")