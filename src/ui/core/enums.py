from enum import StrEnum


class Template(StrEnum):
    LOGIN = "modules/auth/login.html"
    SIGNUP = "modules/auth/signup.html"
    INDEX = "modules/index.html"
    DASHBOARD = "modules/dashboard.html"
    PROGRAMS = "modules/programs.html"


class View(StrEnum):
    DASHBOARD = "ui.dashboard.navigate_to_dashboard"
    LOGIN = "ui.auth.login_page"
