from db import get_connection

a = get_connection()
c = a.cursor()

# c.execute("""
# CREATE TABLE tasks (
#     task_id INTEGER PRIMARY KEY AUTOINCREMENT,
# task TEXT NOT NULL,
# complete INTEGER DEFAULT 0
# )
# """)

# c.execute("""
# CREATE TABLE users (
#     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT UNIQUE NOT NULL,
#     password_hash TEXT NOT NULL
# )
# """)

# c.execute("""ALTER TABLE tasks RENAME TO tasks_old""")

c.execute("""
CREATE TABLE tasks(
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    complete INTEGER DEFAULT 0,
    user_id INTEGER NOT NULL DEFAULT 1, FOREIGN KEY (user_id) REFERENCES users(user_id)
);""")

# c.execute('ALTER TABLE users RENAME to users_old')

a.close()

