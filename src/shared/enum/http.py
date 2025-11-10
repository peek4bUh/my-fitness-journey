# HTTP request methods
from enum import Enum, IntEnum


class HTTP:
    class Method(str, Enum):
        DELETE = "DELETE"
        GET = "GET"
        POST = "POST"
        PUT = "PUT"

    class Status(IntEnum):
        OK = 200
        CREATED = 201
        BAD_REQUEST = 400
        UNAUTHORIZED = 401
        FORBIDDEN = 403
        NOT_FOUND = 404
        CONFLICT = 409
