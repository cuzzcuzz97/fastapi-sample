"""add foreign-key to posts table '


Revision ID: 41306a01f987
Revises: ec610220530b
Create Date: 2022-11-12 13:37:24.253256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41306a01f987'
down_revision = 'ec610220530b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk',  source_table="posts", referent_table="users", local_cols=["owner_id"],remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
