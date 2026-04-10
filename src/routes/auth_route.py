from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.database.connection import get_session
from src.services.auth_service import AuthService
from src.dto.auth_dto import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, session: Session = Depends(get_session)):
    service = AuthService(session)
    return service.login(payload)