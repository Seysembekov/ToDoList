import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "tasks.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)
#
# c.execute("""
# CREATE TABLE tasks (
#     task_id INTEGER PRIMARY KEY AUTOINCREMENT,
# task TEXT NOT NULL,
# complete INTEGER DEFAULT 0
# )
# """)

