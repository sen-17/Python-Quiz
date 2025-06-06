from termcolor import colored

print(colored("🌟 Welcome to the Python Quiz! 🌟", "yellow"))
print("Answer the following questions by typing the letter of the correct answer.")

questions = [
    {
        "question": "1. What is the capital city of Indonesia?",
        "options": {
            "A": "Jakarta",
            "B": "Bandung",
            "C": "Surabaya"
        },
        "answer": "A"
    },
    {
        "question": "2. What is 5 x 12?",
        "options": {
            "A": "60",
            "B": "50",
            "C": "70"
        },
        "answer": "A"
    },
    {
        "question": "3. What is the largest planet in our solar system?",
        "options": {
            "A": "Earth",
            "B": "Jupiter",
            "C": "Saturn"
        },
        "answer": "B"
    }
]

score = 0 

for question in questions:
    print("\n" + question["question"]) # print the question 

    for option, text in question["options"].items():
        print(f"{option}: {text}") # print the options

    user_answer = input("Your answer (A,B or C): ").upper()

    if user_answer == question["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer is {question['answer']}.")

print(f"\nYour final score is {score} out of {len(questions)}.")
if score == len(questions):
    print("🎉 Congratulations! You answered all questions correctly!")
else:
    print("Better luck next time! Keep practicing to improve your score.")