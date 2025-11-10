from enum import StrEnum


class Template(StrEnum):
    LOGIN = "auth/login.html"
    SIGNUP = "auth/signup.html"
    INDEX = "index.html"
    DASHBOARD = "dashboard.html"
