class Users:
    def __init__(self, username: str, password_hash: str, user_id: int | None = None):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash