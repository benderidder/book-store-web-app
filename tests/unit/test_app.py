import pytest
from app import create_app
from app.data.models import Book
from app.extensions import db

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()  # Create the app instance

    # Create the database if needed and set up the testing context
    with app.app_context():
        yield app  # Yield the app instance for testing, then tear down

@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()

def test_app_initialization(app):
    """Test if the app is initialized properly."""
    # assert app.config['ENV'] == 'production'  # Adjust based on your config
    assert app.config['DEBUG'] is False       # Adjust based on your config

def test_extensions_initialization(app):
    """Test if extensions are initialized."""
    assert db is not None
    assert hasattr(app, 'extensions')  # Check that extensions are registered

def test_blueprints_registration(app):
    """Test if blueprints are registered."""
    assert 'home' in app.blueprints
    assert 'books' in app.blueprints
    assert 'authors' in app.blueprints

def test_database_migrations(app):
    """Test database migrations."""
    with app.app_context():
        db.create_all()  # Prepare the database
        # You can add checks to validate migration success if needed.

def test_seed_data(app):
    """Test if seed data is initialized correctly."""
    with app.app_context():
        # Validate the seeding process, e.g., check if data exists.
        # This assumes you have some method to verify seeded data.
        assert db.session.query(Book).count() > 0  # Replace SomeModel with the actual model used for seeding
