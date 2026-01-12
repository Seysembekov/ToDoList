from fastapi import APIRouter, HTTPException
from services.userService import UserService

router = APIRouter(prefix="/auth", tags=["Auth"])
service = UserService()

@router.post("/register")
def register(username: str, password: str):
    try:
        service.register(username, password)
        return {"status": "ok"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(username: str, password: str):
    try:
        token = service.login(username, password)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError:
        raise HTTPException(status_code=401, detail="invalid credentials")