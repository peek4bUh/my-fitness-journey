from enum import StrEnum


class Template(StrEnum):
    LOGIN = "auth/login.html"
    SIGNUP = "auth/signup.html"
    INDEX = "index.html"
    DASHBOARD = "dashboard.html"
    PROGRAMS = "programs.html"


class View(StrEnum):
    DASHBOARD = "ui.dashboard.navigate_to_dashboard"
    LOGIN = "ui.auth.login_page"
