from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from uuid import UUID


# ---------- Request Schemas (data coming IN) ----------

class UserRegister(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ---------- Response Schemas (data going OUT) ----------

class UserResponse(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True  # allows Pydantic to read data from SQLAlchemy objects


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"