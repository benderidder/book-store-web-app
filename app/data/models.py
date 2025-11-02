from flask_sqlalchemy import SQLAlchemy

from app.extensions import db  # Adjust the import based on your structure

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=True)
    author = db.relationship('Author', backref=db.backref('books', lazy=True))

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
