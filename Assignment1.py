# List of quiz questions
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "correct_answer": "A"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. HTML", "D. All of the above"],
        "correct_answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Control Processing Unit"],
        "correct_answer": "B"
    }
]

score = 0

# Loop through questions
for q in quiz:
    print("\n" + q["question"])
    
    for option in q["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == q["correct_answer"]:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong ❌")

# Function to calculate result
def show_result(score, total):
    percentage = (score / total) * 100
    print("\nYour score:", score, "/", total)
    print("Percentage:", percentage, "%")

    if percentage >= 50:
        print("You passed 🎉")
    else:
        print("You failed 📚")

# Call the function
show_result(score, len(quiz))