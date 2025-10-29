from flask import Flask
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

    app.register_blueprint(home)
    app.register_blueprint(books)

    # optional: seed data
    from app.seed import seed_data
    with app.app_context():
        seed_data()

    return app