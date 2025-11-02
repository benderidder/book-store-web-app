from flask import Blueprint, render_template, request, redirect, url_for
from app.extensions import db
from app.data.models import Book
from app.services.book_service import BookService

books = Blueprint('books', __name__, url_prefix='/books')
book_service = BookService(db.session)

@books.route('/')
def list():
    data = book_service.get_all_books()
    return render_template('/books/list.html', data=data)

@books.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        book_service.create_book(request.form['title'])
        return redirect(url_for('books.list'))
    return render_template('/books/create.html')

@books.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    book = book_service.get_book(book_id)
    if request.method == 'POST':
        book_service.update_book(book, request.form['title'])
        return redirect(url_for('books.list'))
    return render_template('books/edit.html', book=book)

@books.route('/delete/<int:book_id>', methods=['POST'])
def delete(book_id):
    book = book_service.get_book(book_id)
    if book:
        book_service.delete_book(book)
    return redirect(url_for('books.list'))