
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from auth.oauth2 import get_current_user
from auth.utils import get_password_hash
from config.database import get_db
from decorators.check_role import has_role
from models.user import User, Role
from schemas.enum import UserRole
from schemas.user import UserReq, UserCreateRes

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get('/', status_code=status.HTTP_200_OK,
            response_model=List[UserCreateRes])
@has_role(['SUPER_ADMIN'])
async def get_user(
        search: Optional[str] = '',
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    print(UserRole.SUPER_ADMIN.value)
    res = db.query(User).filter(User.username.ilike(f'%{search}%')).all()
    return res


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserReq)
async def add_user(user: UserReq, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password
    new_user = User(**user.dict())
    default_role = db.query(Role).filter(Role.name == UserRole.USER).all()
    if default_role:
        new_user.roles = default_role
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
