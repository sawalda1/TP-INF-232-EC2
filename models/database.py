import sqlite3
from config import DATABASE

def get_connection():
    return sqlite3.connect(DATABASE)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evaluations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cours TEXT,
        note_cours REAL,
        clarte REAL,
        organisation REAL,
        difficulte REAL
    )
    """)

    conn.commit()
    conn.close()