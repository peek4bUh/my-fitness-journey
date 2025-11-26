from enum import StrEnum


class Template(StrEnum):
    LOGIN = "modules/auth/login.j2"
    SIGNUP = "modules/auth/signup.j2"
    INDEX = "modules/home/index.j2"
    OVERVIEW = "modules/dashboard/overview.j2"
    PROGRAMS = "modules/dashboard/programs.j2"


class View(StrEnum):
    DASHBOARD_OVERVIEW = "ui.dashboard.dashboard_overview_page"
    LOGIN = "ui.auth.login_page"
    REGISTER = "ui.auth.signup_page"
