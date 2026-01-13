from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from models.config import SECRET_KEY, ALGORITHM
from repositories.user_repo import UserRepo
from models.users import Users

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    repo = UserRepo()
    row = repo.get_by_id(user_id)
    if not row:
        raise HTTPException(status_code=401, detail="user not found")

    return Users(
        user_id=row[0],
        username=row[1],
        password_hash=row[2]
    )