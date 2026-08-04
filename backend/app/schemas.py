from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from uuid import UUID
from typing import List


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
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ---------- Role Schemas ----------

class RoleListItem(BaseModel):
    id: UUID
    title: str
    slug: str
    average_salary: str

    class Config:
        from_attributes = True


class RoleDetail(BaseModel):
    id: UUID
    title: str
    slug: str
    job_description: str
    skills_required: List[str]
    hiring_companies: List[str]
    average_salary: str
    learning_roadmap: List[str]
    interview_pattern: str
    created_at: datetime

    class Config:
        from_attributes = True