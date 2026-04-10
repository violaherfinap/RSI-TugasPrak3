# auth_service.py
from fastapi import HTTPException, status
from sqlmodel import Session
from passlib.exc import UnknownHashError

from src.repositories.auth_repository import AuthRepository
from src.dto.auth_dto import LoginRequest, TokenResponse
from src.utils.security import verify_password, create_access_token

class AuthService:
    def __init__(self, session: Session):
        self.repo = AuthRepository(session)

    def login(self, payload: LoginRequest) -> TokenResponse:
        account = self.repo.find_by_email_or_username(payload.identifier)

        if not account:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email/username atau password salah"
            )

        try:
            password_valid = verify_password(payload.password, account.password)
        except UnknownHashError:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Sistem autentikasi belum siap, password belum di-hash." # TUNGGU VIO
            )

        if not password_valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email/username atau password salah"
            )

        token_data = {
            "sub": str(account.id),
            "user_id": account.user_id,
            "role": account.role.name if account.role else None,
        }

        token = create_access_token(token_data)

        return TokenResponse(
            access_token=token,
            account_id=account.id,
            user_id=account.user_id,
            role=account.role.name if account.role else ""
        )