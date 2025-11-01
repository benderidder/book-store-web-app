from app.extensions import db
from flask import Blueprint, render_template
from app.services.author_service import AuthorService

authors = Blueprint('authors', __name__, url_prefix='/authors')
author_service = AuthorService(db.session)

@authors.route('/')
def list():
    data = author_service.get_all_authors()
    return render_template('/authors/list.html', data=data)

@authors.route('/create', methods=['GET', 'POST'])
def create():
    from flask import request, redirect, url_for
    if request.method == 'POST':
        author_service.create_author(request.form['name'])
        return redirect(url_for('authors.list'))
    return render_template('/authors/create.html')

@authors.route('/edit/<int:author_id>', methods=['GET', 'POST'])
def edit(author_id):    
    from flask import request, redirect, url_for
    author = author_service.get_author(author_id)
    if request.method == 'POST':
        author_service.update_author(author, request.form['name'])
        return redirect(url_for('authors.list'))
    return render_template('authors/edit.html', author=author)

@authors.route('/delete/<int:author_id>', methods=['POST'])
def delete(author_id):  
    from flask import redirect, url_for
    author = author_service.get_author(author_id)
    if author:
        author_service.delete_author(author)
    return redirect(url_for('authors.list'))