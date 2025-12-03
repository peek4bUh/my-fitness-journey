from enum import StrEnum


class Template(StrEnum):
    LOGIN = "auth/login.j2"
    SIGNUP = "auth/signup.j2"
    INDEX = "home/index.j2"
    OVERVIEW = "dashboard/overview.j2"
    PROGRAMS = "dashboard/programs.j2"


class View(StrEnum):
    DASHBOARD_OVERVIEW = "ui.dashboard.dashboard_overview_page"
    LOGIN = "ui.auth.login_page"
    REGISTER = "ui.auth.signup_page"
