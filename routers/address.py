from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from config.database import get_db
from models.user import Address
from schemas.user import AddressRes, AddressReq

router = APIRouter(
    prefix="/address",
    tags=["address"]
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[AddressRes])
async def get_address(db: Session = Depends(get_db)):
    res = db.query(Address).all()
    return res


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_address(address: AddressReq, db: Session = Depends(get_db)):
    new_address = Address(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address
