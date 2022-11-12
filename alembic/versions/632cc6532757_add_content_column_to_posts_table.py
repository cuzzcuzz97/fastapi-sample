"""add content column to posts table

Revision ID: 632cc6532757
Revises: 9d3daf2c9f39
Create Date: 2022-11-12 12:58:34.574059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '632cc6532757'
down_revision = '9d3daf2c9f39'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
