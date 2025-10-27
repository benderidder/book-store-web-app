from app.models import db, Book

def seed_data():
    with db.session.begin():
        # Check if the table is empty
        if Book.query.count() == 0:
            # Insert sample data
            books = [
                Book(title="The Great Gatsby"),
                Book(title="To Kill a Mockingbird"),
                Book(title="1984"),
                Book(title="Pride and Prejudice")
            ]
            db.session.bulk_save_objects(books)  # Efficiently add multiple objects
            db.session.commit()  # Commit the transaction
            print("Seed data inserted!")
        else:
            print("Table already populated.")
