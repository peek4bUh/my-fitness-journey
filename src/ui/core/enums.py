from enum import StrEnum


class Template(StrEnum):
    LOGIN = "modules/auth/login.html"
    SIGNUP = "modules/auth/signup.html"
    INDEX = "modules/home/index.html"
    DASHBOARD = "modules/dashboard/dashboard.html"
    PROGRAMS = "modules/dashboard/programs.html"


class View(StrEnum):
    DASHBOARD = "ui.dashboard.navigate_to_dashboard"
    LOGIN = "ui.auth.login_page"
