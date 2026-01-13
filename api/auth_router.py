from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
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
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        token = service.login(
            form_data.username,
            form_data.password
        )
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    except ValueError:
        raise HTTPException(status_code=401, detail="invalid credentials")