from models.users import Users
from db.db import get_connection

class UserRepo:
    def __init__(self):
        self.model = Users

    def createAcc(self, user: Users):
        conn = get_connection()
        c = conn.cursor()

        c.execute(
            "INSERT INTO users(username, password_hash) VALUES(?, ?)",
            (user.username, user.password_hash)
        )

        conn.commit()
        conn.close()

    def getByName(self, username: str):
        conn = get_connection()
        c = conn.cursor()

        c.execute(
            "SELECT user_id, username, password_hash FROM users WHERE username = ?",
            (username,)  # ← ВАЖНО
        )

        a = c.fetchone()
        conn.close()
        return a

    def getById(self, user_id: int):
        conn = get_connection()
        c = conn.cursor()

        c.execute(
            "SELECT user_id, username, password_hash FROM users WHERE user_id = ?",
            (user_id,)
        )

        a = c.fetchone()
        conn.close()
        return a

    def existsByUsername(self, username: str) -> bool:
        conn = get_connection()
        c = conn.cursor()

        c.execute(
            "SELECT 1 FROM users WHERE username = ? LIMIT 1",
            (username,)
        )

        exists = c.fetchone() is not None
        conn.close()
        return exists