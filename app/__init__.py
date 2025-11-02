from flask import Flask
from flask_migrate import upgrade
from app.config import Config
from app.extensions import db, migrate

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints (import inside to avoid circular imports)
    from app.controllers.home_controller import home
    from app.controllers.books_controller import books
    from app.controllers.authors_controller import authors

    app.register_blueprint(home)
    app.register_blueprint(books)
    app.register_blueprint(authors)

    # apply database migrations and seed data
    from app.data.seed import seed_data
    with app.app_context():
        upgrade()
        seed_data()

    return app