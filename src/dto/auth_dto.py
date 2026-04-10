from pydantic import BaseModel

class LoginRequest(BaseModel):
    identifier: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    account_id: int
    user_id: int
    role: str