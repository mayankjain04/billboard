from flask import redirect, session, render_template
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return render_template("login.html", message="Login is required to view this page.")
        return f(*args, **kwargs)

    return decorated_function