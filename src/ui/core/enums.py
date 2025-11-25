from enum import StrEnum


class Template(StrEnum):
    LOGIN = "modules/auth/login.html"
    SIGNUP = "modules/auth/signup.html"
    INDEX = "modules/home/index.html"
    OVERVIEW = "modules/dashboard/overview.html"
    PROGRAMS = "modules/dashboard/programs.html"


class View(StrEnum):
    DASHBOARD_OVERVIEW = "ui.dashboard.dashboard_overview_page"
    LOGIN = "ui.auth.login_page"
