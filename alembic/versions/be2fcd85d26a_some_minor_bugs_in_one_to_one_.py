"""some minor bugs in one-to-one relationship

Revision ID: be2fcd85d26a
Revises: e3deb6f602a9
Create Date: 2024-04-15 17:36:24.256442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be2fcd85d26a'
down_revision: Union[str, None] = 'e3deb6f602a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'addresses', ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'addresses', type_='unique')
    # ### end Alembic commands ###
