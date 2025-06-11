import sqlite3

from utils.files import get_file_data
from constants import DB_NAME


def create_database(sql_file: str) -> None:
    """Creates the database and executes SQL statements from the provided SQL file."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        sql_data = get_file_data(sql_file)
        cursor.executescript(sql_data)
        conn.commit()
        print("Database and tables created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()


def insert_exercise_data(exercise: str, sets_data: str) -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    sql = "INSERT INTO exercises (name, set_data) VALUES (?, ?)"
    cursor.execute(sql, (exercise, sets_data))

    conn.commit()
    conn.close()

    print(f"Data inserted for exercise: {exercise}")
