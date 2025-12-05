from enum import StrEnum


class Template(StrEnum):
    LOGIN = "auth/login.html.j2"
    SIGNUP = "auth/signup.html.j2"
    INDEX = "home/index.html.j2"
    OVERVIEW = "dashboard/overview.html.j2"
    PROGRAM = "dashboard/program.html.j2"
    PROGRAMS = "dashboard/programs.html.j2"


class View(StrEnum):
    LOGIN = "ui.auth.login_page"
    REGISTER = "ui.auth.signup_page"
    DASHBOARD_OVERVIEW = "ui.dashboard.dashboard_overview_page"
    DASHBOARD_PROGRAMS = "ui.dashboard.dashboard_programs_page"
