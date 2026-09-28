import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "questions.json"


def load_questions():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def run_quiz():
    questions = load_questions()
    score = 0

    print("\n=== QUIZ LAB ===")
    print("Answer using A, B, C or D.\n")

    for number, item in enumerate(questions, start=1):
        print(f"{number}. {item['question']}")
        for key, option in item["options"].items():
            print(f"   {key}. {option}")

        answer = input("Your answer: ").strip().upper()

        if answer == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {item['answer']}\n")

    accuracy = (score / len(questions)) * 100 if questions else 0
    print(f"Final score: {score}/{len(questions)}")
    print(f"Accuracy: {accuracy:.1f}%")
