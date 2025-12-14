from functools import wraps
from flask import redirect, url_for, flash
from flask_login import LoginManager, current_user

login_manager = LoginManager()
login_manager.login_view = "auth.login"


def role_required(*roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for("auth.login"))
            if current_user.role not in roles:
                flash("You do not have permission to access this page.", "error")
                return redirect(url_for("main.home"))
            return fn(*args, **kwargs)
        return wrapper
    return decorator
