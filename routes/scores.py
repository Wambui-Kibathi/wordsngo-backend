from flask import Blueprint, jsonify, request
from extensions import db
from models import Score  # You need a Score model in models.py

scores_bp = Blueprint('scores', __name__, url_prefix='/scores')

# Get all scores
@scores_bp.route('/', methods=['GET'])
def get_scores():
    scores = Score.query.all()
    results = []
    for s in scores:
        results.append({
            "id": s.id,
            "user_id": s.user_id,
            "score": s.score,
            "date": s.date
        })
    return jsonify(results)

# Add a new score
@scores_bp.route('/', methods=['POST'])
def add_score():
    data = request.get_json()
    new_score = Score(
        user_id=data['user_id'],
        score=data['score']
    )
    db.session.add(new_score)
    db.session.commit()
    return jsonify({"message": "Score added!", "id": new_score.id}), 201
