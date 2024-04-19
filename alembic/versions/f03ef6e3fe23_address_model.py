"""address model

Revision ID: f03ef6e3fe23
Revises: 23fa61181740
Create Date: 2024-04-13 16:49:06.740587

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f03ef6e3fe23'
down_revision: Union[str, None] = '23fa61181740'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('addresses', sa.Column('user_id', sa.UUID(), nullable=True))
    op.create_foreign_key(None, 'addresses', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'addresses')
    op.drop_column('addresses', 'user_id')
    # ### end Alembic commands ###
