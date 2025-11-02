from typing import List

from app.data.view_models import BookViewModel

class BookService:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_book(self, title, author_id):
        from ..data.models import Book  # Import here to avoid circular imports
        new_book = Book(title=title, author_id=author_id)
        self.db_session.add(new_book)
        self.db_session.commit()
        return new_book
    
    def get_book(self, book_id):
        from ..data.models import Book  # Import here to avoid circular imports
        return self.db_session.query(Book).get(book_id)

    def get_all_books(self) -> List[BookViewModel]:
        from ..data.models import Book, Author
        # return lightweight viewmodels via a single SQL query (outer join)
        rows = (
            self.db_session
                .query(Book, Author)
                .outerjoin(Author, Book.author_id == Author.id)
                .all()
        )
        result: List[BookViewModel] = []
        
        for book, author in rows:
            author_name = author.name if author else ''
            result.append(BookViewModel(id=book.id, title=book.title, author_name=author_name))

        return result

    def update_book(self, book, title):
        book.title = title
        self.db_session.commit()
        
    def delete_book(self, book):
        self.db_session.delete(book)
        self.db_session.commit()