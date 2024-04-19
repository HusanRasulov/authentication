from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from auth.oauth2 import create_access_token
from auth.utils import verify
from config.database import get_db
from models.user import User
from schemas.user import Token, loginReq

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login', response_model=Token)
def login(user_credentials: loginReq, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    access_token = create_access_token(data={"user_id": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}
