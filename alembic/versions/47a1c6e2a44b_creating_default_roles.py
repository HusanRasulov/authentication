"""creating default roles

Revision ID: 47a1c6e2a44b
Revises: 2d84af27a45d
Create Date: 2024-04-17 19:50:31.936675

"""
from typing import Sequence, Union

from alembic import op

from models.user import Role
from schemas.enum import UserRole

# revision identifiers, used by Alembic.
revision: str = '47a1c6e2a44b'
down_revision: Union[str, None] = '2d84af27a45d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        Role.__table__,
        [{'name': role.name} for role in UserRole])


def downgrade() -> None:
    op.execute(Role.__table__.delete())
    pass
