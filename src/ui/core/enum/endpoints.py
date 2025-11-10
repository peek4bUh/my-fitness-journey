from enum import StrEnum


class Endpoint(StrEnum):
    REGISTER = "/register"
    LOGOUT = "/logout"
    LOGIN = "/login"
    DASHBOARD = "/dashboard"
    INDEX = "/"
    HOME = "/home"
