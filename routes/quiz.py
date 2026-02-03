from flask import Blueprint, jsonify, request
from extensions import db
from models import Question

quiz_bp = Blueprint('quiz', __name__, url_prefix='/quiz')

# Get all questions
@quiz_bp.route('/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    results = []
    for q in questions:
        results.append({
            "id": q.id,
            "text": q.text,
            "choices": q.choices,
            "answer": q.answer,
            "topic": q.topic,
            "difficulty": q.difficulty
        })
    return jsonify(results)

# Submit answers (placeholder, you can extend to scoring)
@quiz_bp.route('/submit', methods=['POST'])
def submit_quiz():
    data = request.get_json()
    # Example: data = {"user_id": 1, "answers": [{"question_id":1, "answer":0}, ...]}
    # For now, just echo back
    return jsonify({"message": "Quiz submitted!", "data": data}), 200
