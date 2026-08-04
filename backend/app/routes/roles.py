import json
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Role
from app.schemas import RoleListItem, RoleDetail

router = APIRouter(prefix="/roles", tags=["Career Roadmap"])


def _parse_role_detail(role: Role) -> dict:
    return {
        "id": role.id,
        "title": role.title,
        "slug": role.slug,
        "job_description": role.job_description,
        "skills_required": json.loads(role.skills_required),
        "hiring_companies": json.loads(role.hiring_companies),
        "average_salary": role.average_salary,
        "learning_roadmap": json.loads(role.learning_roadmap),
        "interview_pattern": role.interview_pattern,
        "created_at": role.created_at,
    }


@router.get("", response_model=list[RoleListItem])
def list_roles(db: Session = Depends(get_db)):
    roles = db.query(Role).order_by(Role.title).all()
    return roles


@router.get("/{slug}", response_model=RoleDetail)
def get_role(slug: str, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.slug == slug).first()
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found",
        )
    return _parse_role_detail(role)