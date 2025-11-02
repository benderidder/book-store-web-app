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
                .query(
                    Book.id.label('id'),
                    Book.title.label('title'),
                    Author.name.label('author_name')
                )
                .outerjoin(Author, Book.author_id == Author.id)
                .all()
        )
        result: List[BookViewModel] = []
        for r in rows:
            # SQLAlchemy row supports attribute access for labeled columns
            author = getattr(r, 'author_name', None) or ''
            result.append(BookViewModel(id=r.id, title=r.title, author_name=author))
        return result

    def update_book(self, book, title):
        book.title = title
        self.db_session.commit()
        
    def delete_book(self, book):
        self.db_session.delete(book)
        self.db_session.commit()