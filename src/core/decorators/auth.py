from functools import wraps
from flask import session, redirect, url_for

from core.constants.pages import PAGE_DASHBOARD, PAGE_LOGIN


def redirect_if_authenticated():
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if session.get("user"):
                return redirect(url_for(PAGE_DASHBOARD))
            return f(*args, **kwargs)
        return wrapped
    return decorator


def is_user_logged():
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not session.get("user"):
                return redirect(url_for(PAGE_LOGIN))
            return f(*args, **kwargs)
        return wrapped
    return decorator
