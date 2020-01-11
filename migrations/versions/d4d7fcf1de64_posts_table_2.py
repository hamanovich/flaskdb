"""posts table 2

Revision ID: d4d7fcf1de64
Revises: c686e6b79f0f
Create Date: 2020-01-11 23:48:09.337046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4d7fcf1de64'
down_revision = 'c686e6b79f0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    # ### end Alembic commands ###