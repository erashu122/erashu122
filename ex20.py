#Number gussing game
import random
lowest_number = 1
highest_number = 100
answer= random.randint(lowest_number,highest_number)
guesses = 0
is_runing = True

print ("Welcome to the number guessing game!")
print (f"Guess a number between {lowest_number} and {highest_number}")

while is_runing:
    guess=input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_number or guess > highest_number:
            print("That number is outof range")
            print(f"Please enter a number between {lowest_number} and {highest_number}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"CORRECT! The number was {answer}")
            is_runing = False
            print(f"Congratulations! You guessed the number in {guesses} guesses")
    else:
        print("Please enter a valid number")
        print(f"Please enter a number between {lowest_number} and {highest_number}")
print("----------------")
print("-----Thanks for playing!-----")    


