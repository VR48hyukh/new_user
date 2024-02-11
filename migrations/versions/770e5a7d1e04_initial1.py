"""Initial1

Revision ID: 770e5a7d1e04
Revises: 
Create Date: 2024-02-03 20:27:23.988015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '770e5a7d1e04'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('permissions', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('customers')
    op.drop_table('orders')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('shipp_date', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('order_date', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('order_name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('order_id', name='orders_pkey')
    )
    op.create_table('customers',
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('company_name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('contact_name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('contact_title', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('adress', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('city', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('region', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('country', sa.TEXT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('customer_id', name='customers_pkey')
    )
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###
