"""empty message

Revision ID: f91be06ebb5b
Revises: ed1dd9a0829f
Create Date: 2020-01-11 23:52:47.627992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f91be06ebb5b'
down_revision = 'ed1dd9a0829f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('user', 'password_hash',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('user', 'password_hash',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###
