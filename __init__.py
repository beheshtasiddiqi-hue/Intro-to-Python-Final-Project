from flask import Flask
from flask_login import current_user
from app.extensions import db, migrate, login_manager


def create_app():
    app = Flask(__name__)

    # --------------------
    # App Configuration
    # --------------------
    app.config["SECRET_KEY"] = "dev-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # --------------------
    # Initialize Extensions
    # --------------------
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # --------------------
    # Make current_user available in templates
    # --------------------
    @app.context_processor
    def inject_current_user():
        return {"current_user": current_user}

    # --------------------
    # Load Models
    # --------------------
    from app import models  # noqa: F401
    from app.models.user import User

    # --------------------
    # Flask-Login user loader
    # --------------------
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # --------------------
    # Register Blueprints
    # --------------------
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.routes.books import books_bp
    app.register_blueprint(books_bp)

    from app.routes.loans import loans_bp
    app.register_blueprint(loans_bp)

    from app.routes.admin import admin_bp
    app.register_blueprint(admin_bp)

    return app


