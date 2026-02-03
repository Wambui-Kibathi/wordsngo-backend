import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from extensions import db, migrate  # import the shared instances

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models after db.init_app
    from models import Question, User, Score

    # Import routes
    from routes.auth import auth_bp
    from routes.quiz import quiz_bp
    from routes.scores import scores_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(scores_bp)

    @app.route("/")
    def home():
        return {"message": "WordsnGo backend running!"}

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
