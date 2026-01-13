from db.db import get_connection
from models.users import Users

class UserRepo:

    def create(self, user: Users):
        conn = get_connection()
        c = conn.cursor()
        c.execute(
            "INSERT INTO users(username, password_hash) VALUES (?, ?)",
            (user.username, user.password_hash)
        )
        conn.commit()
        conn.close()

    def get_by_username(self, username: str):
        conn = get_connection()
        c = conn.cursor()
        c.execute(
            "SELECT user_id, username, password_hash FROM users WHERE username = ?",
            (username,)
        )
        row = c.fetchone()
        conn.close()
        return row

    def get_by_id(self, user_id: int):
        conn = get_connection()
        c = conn.cursor()
        c.execute(
            "SELECT user_id, username, password_hash FROM users WHERE user_id = ?",
            (user_id,)
        )
        row = c.fetchone()
        conn.close()
        return row

    def exists_by_username(self, username: str) -> bool:
        conn = get_connection()
        c = conn.cursor()
        c.execute(
            "SELECT 1 FROM users WHERE username = ? LIMIT 1",
            (username,)
        )
        exists = c.fetchone() is not None
        conn.close()
        return exists