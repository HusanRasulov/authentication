import uuid
from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str
    username: str
    email: str
    password: str


class AddressBase(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4)


class AddressRes(AddressBase):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)


class UserCreateRes(UserBase):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    address: Optional[AddressRes]


class AddressReq(AddressBase):
    pass


class UserReq(UserBase):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class loginReq(BaseModel):
    username: str
    password: str
