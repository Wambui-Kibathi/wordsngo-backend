import requests
import random
from app import create_app
from extensions import db
from models import Question

# Create Flask app and push app context
app = create_app()
with app.app_context():
    CATEGORY_MAPPING = {
        "General Knowledge": "General Knowledge",
        "Entertainment: Film": "Entertainment",
        "Entertainment: Music": "Entertainment",
        "Entertainment: Television": "Entertainment",
        "Entertainment: Video Games": "Entertainment",
        "Entertainment: Board Games": "Entertainment",
        "Science & Nature": "General Knowledge",
        "Arts": "Art",
        "Literature": "Literature",
    }

    def map_category(category):
        return CATEGORY_MAPPING.get(category, "General Knowledge")

    def fetch_questions(amount=50):
        url = f"https://opentdb.com/api.php?amount={amount}&type=multiple"
        response = requests.get(url)
        data = response.json()
        if data["response_code"] != 0:
            raise Exception("Failed to fetch questions from Open Trivia DB")
        return data["results"]

    def seed_database():
        questions_data = fetch_questions(50)
        for item in questions_data:
            choices = item["incorrect_answers"] + [item["correct_answer"]]
            random.shuffle(choices)
            question = Question(
                text=item["question"],
                choices=choices,
                answer=choices.index(item["correct_answer"]),
                topic=map_category(item["category"]),
                difficulty=item["difficulty"].capitalize()
            )
            db.session.add(question)
        db.session.commit()
        print(f"Seeded {len(questions_data)} questions successfully!")

    seed_database()
