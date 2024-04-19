from functools import wraps
from typing import List

from fastapi import Depends, HTTPException
from starlette import status

from auth.oauth2 import get_current_user
from models.user import User


def has_role(allowed_roles: List[str]):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, current_user: User = Depends(get_current_user), **kwargs):
            user_roles = [role.name for role in current_user.roles]
            if not any(role in user_roles for role in allowed_roles):
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied")
            return await func(*args, **kwargs)

        return wrapper

    return decorator
