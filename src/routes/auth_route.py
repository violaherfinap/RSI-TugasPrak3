from fastapi import APIRouter, HTTPException
from src.services.auth_service import register_new_account
from src.dto.auth_dto import RegisterRequest

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(user_data: RegisterRequest):
    try:
        result = register_new_account(user_data.dict())
        return {
            "message": "Registrasi berhasil",
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))