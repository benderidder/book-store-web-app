import pytest
from unittest.mock import MagicMock, create_autospec
from app.services.author_service import AuthorService
from app.data.models import Author

@pytest.fixture
def db_session_mock():
    # Create a mock for the database session
    mock_db_session = create_autospec(MagicMock)
    mock_db_session.add = MagicMock()
    mock_db_session.commit = MagicMock()
    mock_db_session.delete = MagicMock()
    mock_db_session.query = MagicMock()
    
    return mock_db_session

@pytest.fixture
def author_service(db_session_mock):
    return AuthorService(db_session=db_session_mock)

def test_create_author(author_service, db_session_mock):
    # Arrange
    name = "Test Author"
    
    # Act
    new_author = author_service.create_author(name)

    # Assert
    db_session_mock.add.assert_called_once()
    db_session_mock.commit.assert_called_once()
    assert isinstance(new_author, Author)
    assert new_author.name == name

def test_get_author(author_service, db_session_mock):
    # Arrange
    author_id = 1
    expected_author = Author(id=author_id, name="Test Author")
    
    db_session_mock.query.return_value.get.return_value = expected_author

    # Act
    result = author_service.get_author(author_id)

    # Assert
    db_session_mock.query.assert_called_once()
    assert result == expected_author

def test_get_all_authors(author_service, db_session_mock):
    # Arrange
    authors_data = [Author(id=1, name="Author 1"), Author(id=2, name="Author 2")]
    db_session_mock.query.return_value.all.return_value = authors_data
    
    # Act
    authors = author_service.get_all_authors()

    # Assert
    assert len(authors) == 2
    assert authors[0].name == "Author 1"
    assert authors[1].name == "Author 2"

def test_update_author(author_service, db_session_mock):
    # Arrange
    author = Author(id=1, name="Old Name")
    new_name = "New Name"
    
    # Act
    author_service.update_author(author, new_name)

    # Assert
    assert author.name == new_name
    db_session_mock.commit.assert_called_once()

def test_delete_author(author_service, db_session_mock):
    # Arrange
    author = Author(id=1, name="Test Author")
    
    # Act
    author_service.delete_author(author)

    # Assert
    db_session_mock.delete.assert_called_once()
    db_session_mock.commit.assert_called_once()
