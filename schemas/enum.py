from enum import Enum


class UserRole(Enum):
    ADMIN = "ROLE_ADMIN"
    USER = "ROLE_USER"
    SUPER_ADMIN = "ROLE_SUPER_ADMIN"
