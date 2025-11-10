from enum import StrEnum


class Endpoint(StrEnum):
    REGISTER = "/register"
    LOGOUT = "/logout"
    LOGIN = "/login"
    DASHBOARD = "/dashboard"
    INDEX = "/"
    HOME = "/home"


class Template(StrEnum):
    LOGIN = "auth/login.html"
    SIGNUP = "auth/signup.html"
    INDEX = "index.html"
    DASHBOARD = "dashboard.html"


class View(StrEnum):
    DASHBOARD = "ui.dashboard.navigate_to_dashboard"
    LOGIN = "ui.auth.login_page"
