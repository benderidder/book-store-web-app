class AuthorService:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_author(self, name):
        from ..models import Author  # Import here to avoid circular imports
        new_author = Author(name=name)
        self.db_session.add(new_author)
        self.db_session.commit()
        return new_author

    def get_author(self, author_id):
        from ..models import Author  # Import here to avoid circular imports
        return self.db_session.query(Author).get(author_id)

    def get_all_authors(self):
        from ..models import Author  # Import here to avoid circular imports
        return self.db_session.query(Author).all()

    def update_author(self, author, name):
        author.name = name
        self.db_session.commit()

    def delete_author(self, author):
        self.db_session.delete(author)
        self.db_session.commit()