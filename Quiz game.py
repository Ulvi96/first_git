questions = [
    "What is your first name?",
    "What is your first surname?",
    "What is your second name?",
    "What is your second surname?",
    "What is your final name?"
]

options = (
    ("A. first name", "B. last name", "C. last surname", "D. second name"),
    ("A. first name", "B. last name", "C. last surname", "D. first surname"),
    ("A. first name", "B. last name", "C. last surname", "D. second name"),
    ("A. first name", "B. last name", "C. second surname", "D. second name"),
    ("A. first name", "B. final name", "C. last surname", "D. second name")
)

answers = ["A", "D", "D", "C", "B"]
guesses = []
score = 0
max_score = len(questions) * 100  # Maximum score based on questions

for index, question in enumerate(questions, start=1):
    print("------------------------------------------")
    print(f"Question {index}: {question}")

    for option in options[index - 1]:
        print(option)

    while True:
        answer = input("\nEnter your answer (A, B, C, or D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid choice. Please enter A, B, C, or D.")

    if answer == answers[index - 1]:
        print("Correct")
        score += 100
    else:
        print("Incorrect")
    guesses.append(answer)

print("\n----- Results -----")
print(f"Correct Answers: {answers}")
print(f"Your Guesses: {guesses}")
print(f"Your Score: {score} out of {max_score}")
