from app.data.models import Author, Book
from app.extensions import db

def seed_data():
    # Insert authors first (books reference author IDs)
    if Author.query.count() == 0:
        authors = [
            Author(name="F. Scott Fitzgerald"),
            Author(name="Harper Lee"),
            Author(name="George Orwell"),
            Author(name="Jane Austen")
        ]
        db.session.add_all(authors)
        db.session.commit()
        print("Author seed data inserted!")
    else:
        print("Author table already populated.")

    # Insert books after authors exist
    if Book.query.count() == 0:
        # build a mapping name -> id to set author_id reliably
        author_map = {a.name: a.id for a in Author.query.all()}
        books_data = [
            ("The Great Gatsby", "F. Scott Fitzgerald"),
            ("To Kill a Mockingbird", "Harper Lee"),
            ("1984", "George Orwell"),
            ("Pride and Prejudice", "Jane Austen")
        ]

        books = []
        for title, author_name in books_data:
            author_id = author_map.get(author_name)
            books.append(Book(title=title, author_id=author_id))

        db.session.add_all(books)
        db.session.commit()
        print("Seed data inserted!")
    else:
        print("Books table already populated.")
