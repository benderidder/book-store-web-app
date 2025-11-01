from app.models import Author, Book
from app.extensions import db

def seed_data():
    with db.session.begin():
        # Check if the table is empty
        if Book.query.count() == 0:
            # Insert sample data
            books = [
                Book(title="The Great Gatsby", author_id=1),
                Book(title="To Kill a Mockingbird", author_id=2),
                Book(title="1984", author_id=3),
                Book(title="Pride and Prejudice", author_id=4)
            ]
            db.session.bulk_save_objects(books)  # Efficiently add multiple objects
            db.session.commit()  # Commit the transaction
            print("Seed data inserted!")
        else:
            print("Table already populated.")

        if Author.query.count() == 0:
            authors = [
                Author(name="F. Scott Fitzgerald"),
                Author(name="Harper Lee"),
                Author(name="George Orwell"),
                Author(name="Jane Austen")
            ]
            db.session.bulk_save_objects(authors)
            db.session.commit()
            print("Author seed data inserted!")
        else:
            print("Author table already populated.")
