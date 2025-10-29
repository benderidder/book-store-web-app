class BookService:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_book(self, title):
        from ..models import Book  # Import here to avoid circular imports
        new_book = Book(title=title)
        self.db_session.add(new_book)
        self.db_session.commit()
        return new_book
    
    def get_book(self, book_id):
        from ..models import Book  # Import here to avoid circular imports
        return self.db_session.query(Book).get(book_id)

    def update_book(self, book, title):
        book.title = title
        self.db_session.commit()
        
    def delete_book(self, book):
        self.db_session.delete(book)
        self.db_session.commit()