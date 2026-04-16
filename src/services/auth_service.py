# auth_service.py
from fastapi import HTTPException, status
from sqlmodel import Session
from passlib.exc import UnknownHashError

from src.repositories.auth_repository import AuthRepository
from src.dto.auth_dto import LoginRequest, TokenResponse, RegisterRequest
from src.utils.security import verify_password, create_access_token, hash_password


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
                detail="Sistem autentikasi belum siap, password belum di-hash."
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

    def register(self, payload: RegisterRequest):
        if not payload.password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password tidak boleh kosong"
            )

        hashed_password = hash_password(payload.password)

        user_data = payload.dict()
        user_data["password"] = hashed_password

        return {
            "username": user_data["username"],
            "email": user_data["email"]
        }