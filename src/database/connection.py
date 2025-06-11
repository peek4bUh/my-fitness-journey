import sqlite3
from constants import DB_NAME


def get_connection():
    """Returns a connection object to the SQLite3 database."""
    return sqlite3.connect(DB_NAME)
