from repositories.user_repo import UserRepo
from models.users import Users
from hashlib import sha256
from jose import jwt
from models.config import SECRET_KEY, ALGORITHM

class UserService:
    def __init__(self):
        self.repo = UserRepo()

    def create(self, username: str, password: str):
        if self.repo.existsByUsername(username):
            raise ValueError('this user exists')

        password_hash = sha256(password.encode()).hexdigest()
        u = Users(username=username, password_hash=password_hash)
        self.repo.createAcc(u)
        return u

    def login(self, username: str, password: str):
        user = self.repo.getByName(username)
        if not user:
            raise ValueError("invalid credentials")

        password_hash = sha256(password.encode()).hexdigest()
        if user[2] != password_hash:
            raise ValueError('invalid credentials')

        token = self.create_access_token(user[0])

        return token

    def create_access_token(self, user_id: int):
        payload = {"user_id": user_id}
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)