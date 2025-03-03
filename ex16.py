# python quiz game 

questions = (
    "What is the capital of India?",
    "Who is the Prime Minister of India?",
    "What is the capital of the USA?",
    "Who is the President of the USA?",
    "What is the capital of the UK?",
    "Who is the Prime Minister of the UK?",
)

options = (
    ("A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"),
    ("A. Narendra Modi", "B. Manmohan Singh", "C. Rahul Gandhi", "D. Sonia Gandhi"),
    ("A. New York", "B. Washington DC", "C. Los Angeles", "D. Chicago"),
    ("A. Barack Obama", "B. Donald Trump", "C. Hillary Clinton", "D. George Bush"),
    ("A. London", "B. Manchester", "C. Liverpool", "D. Birmingham"),
    ("A. Theresa May", "B. Boris Johnson", "C. David Cameron", "D. Tony Blair"),
)

answers = ("A", "A", "B", "B", "A", "B")

guesses = []
score = 0
question_number = 0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_number]:
        print(option)
        
    guess = input("Enter your guess (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"The correct answer is: {answers[question_number]}")
    print(f"Your score is: {score}")
    
    question_number += 1
    
print("-----------------")
print("    RESULTS     ")
print("-----------------")

print("answer:", end="")
for answer in answers:
    print(f" {answer}", end="")
print()

print("guess: ", end="")
for guess in guesses:
    print(f" {guess}", end="")
print()

score = int((score / len(questions)) * 100)
print(f"Your final score is: {score}%")

if score >= 50:
    print("Congratulations! You passed the quiz!")
else:
    print("Sorry! You failed the quiz!")    

print("\nQuiz completed!")
        
