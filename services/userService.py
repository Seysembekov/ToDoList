from hashlib import sha256
from jose import jwt
from repositories.user_repo import UserRepo
from models.users import Users
from models.config import SECRET_KEY, ALGORITHM

class UserService:

    def __init__(self):
        self.repo = UserRepo()

    def register(self, username: str, password: str):
        if self.repo.exists_by_username(username):
            raise ValueError("user already exists")

        password_hash = sha256(password.encode()).hexdigest()
        user = Users(username=username, password_hash=password_hash)
        self.repo.create(user)

    def login(self, username: str, password: str):
        row = self.repo.get_by_username(username)
        if not row:
            raise ValueError("invalid credentials")

        password_hash = sha256(password.encode()).hexdigest()
        if row[2] != password_hash:
            raise ValueError("invalid credentials")

        payload = {"user_id": row[0]}
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return token