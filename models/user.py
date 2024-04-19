import uuid

from sqlalchemy import Column, String, ForeignKey, Table, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from config.database import Base

user_roles_association = Table(
    'user_roles',
    Base.metadata,
    Column('user_id', UUID, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True, default=str(uuid.uuid4)),
    Column('role_id', Integer, ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)
)


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4(), index=True)
    name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    address = relationship("Address", uselist=False, back_populates="user")
    roles = relationship("Role", secondary=user_roles_association, back_populates="users")


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    users = relationship("User", secondary=user_roles_association, back_populates="roles")


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    street = Column(String)
    suite = Column(String)
    city = Column(String)
    zipcode = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), unique=True)
    user = relationship("User", back_populates="address")
