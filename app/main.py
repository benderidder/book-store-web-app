from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# initialize Flask app and load config
app = Flask(__name__)
app.config.from_object(Config)

# initialize database and migration objects
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import app components
from app.seed import seed_data
from app.models import Book
from app.services.book_service import BookService

# Seed initial data
with app.app_context():
    seed_data()

#
# define routes
#
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books')
def books():
    data = Book.query.all()  # Fetch all records from the table
    return render_template('/books/list.html', data=data)

@app.route('/books/create', methods=['GET', 'POST'])
def books_create():
    if request.method == 'POST':
        book_service = BookService(db.session)
        book_service.create_book(request.form['title'])
        return redirect(url_for('books'))
    if request.method == 'GET':
        return render_template('/books/create.html')
    return render_template('/books/create.html')

@app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
def books_edit(book_id):
    book_service = BookService(db.session)
    book = book_service.get_book(book_id)
    if request.method == 'POST':
        book_service.update_book(book, request.form['title'])
        return redirect(url_for('books'))
    if request.method == 'GET':
        return render_template('books/edit.html', book=book)
    return render_template('books/edit.html', book=book)

@app.route('/books/delete/<int:book_id>', methods=['POST'])
def books_delete(book_id):
    book_service = BookService(db.session)
    book = book_service.get_book(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('books'))

# run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
