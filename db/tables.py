from db import get_connection

a = get_connection()
c = a.cursor()

c.execute("""
CREATE TABLE tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
task TEXT NOT NULL,
complete INTEGER DEFAULT 0
)
""")


a.close()

