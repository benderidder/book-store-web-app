import pytest
from unittest.mock import MagicMock, create_autospec
from app.services.book_service import BookService
from app.data.models import Book, Author
from app.data.view_models import BookViewModel

@pytest.fixture
def db_session_mock():
    # Create a mock for the database session
    mock_db_session = create_autospec(MagicMock)
    # Specify the methods that can be called
    mock_db_session.add = MagicMock()
    mock_db_session.commit = MagicMock()
    mock_db_session.delete = MagicMock()
    mock_db_session.query = MagicMock()
    
    return mock_db_session

@pytest.fixture
def book_service(db_session_mock):
    return BookService(db_session=db_session_mock)

def test_create_book(book_service, db_session_mock):
    # Arrange
    title = "Test Book"
    author_id = 1
    
    # Act
    new_book = book_service.create_book(title, author_id)

    # Assert
    db_session_mock.add.assert_called_once()
    db_session_mock.commit.assert_called_once()
    assert isinstance(new_book, Book)
    assert new_book.title == title
    assert new_book.author_id == author_id

def test_get_book(book_service, db_session_mock):
    # Arrange
    book_id = 1
    expected_book = Book(id=book_id, title="Test Book", author_id=1)
    
    db_session_mock.query.return_value.get.return_value = expected_book

    # Act
    result = book_service.get_book(book_id)

    # Assert
    db_session_mock.query.assert_called_once()
    assert result == expected_book

def test_get_all_books(book_service, db_session_mock):
    # Arrange
    mock_author_1 = Author(id=1, name="Author 1")
    mock_author_2 = Author(id=2, name="Author 2")
    mock_book_1 = Book(id=1, title="Test Book 1", author_id=1)
    mock_book_2 = Book(id=2, title="Test Book 2", author_id=2)
    
    # Simulating the return of objects instead of tuples
    db_session_mock.query.return_value.outerjoin.return_value.all.return_value = [(mock_book_1, mock_author_1), (mock_book_2, mock_author_2)]
    
    # Act
    books = book_service.get_all_books()

    # Assert
    assert len(books) == 2
    assert isinstance(books[0], BookViewModel)
    assert books[0].id == 1
    assert books[0].title == "Test Book 1"
    assert books[0].author_name == "Author 1"

def test_update_book(book_service, db_session_mock):
    # Arrange
    book = Book(id=1, title="Old Title", author_id=1)
    new_title = "New Title"
    
    # Act
    book_service.update_book(book, new_title)

    # Assert
    assert book.title == new_title
    db_session_mock.commit.assert_called_once()

def test_delete_book(book_service, db_session_mock):
    # Arrange
    book = Book(id=1, title="Test Book", author_id=1)
    
    # Act
    book_service.delete_book(book)

    # Assert
    db_session_mock.delete.assert_called_once()
    db_session_mock.commit.assert_called_once()
