from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import db, Book  # Import db from models.py
from app.seed import seed_data  # Import the seed function

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/bookstore_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    return app

app = create_app()

with app.app_context():
    seed_data()  # Call the seed function

@app.route('/')
def home():
    data = Book.query.all()  # Fetch all records from the table
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
