from fastapi import APIRouter, HTTPException
from utils.auth import create_access_token
from models.auth_model import AuthRequest
from database.entities.user_dalc import UserDALC
from passlib.context import CryptContext


router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/login")
def login(model:AuthRequest):
    
    if model.username != 'admin' or model.password != "1234":
        raise HTTPException(status_code=401, detail="Credenciales invalidas")

    # Generar Token
    token = create_access_token({"sub":model.username})

    user = UserDALC.get_by_username(model.username)

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales invalidas")

    if user["password"] != model.password:
        raise HTTPException(status_code=401, detail="Credenciales invalidas")


    return {
        "access_token":token,
        "token_type":"bearer",
    }
    