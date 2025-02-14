"""empty message

Revision ID: fec72045e884
Revises: c3191b0280d9
Create Date: 2025-02-14 17:49:31.056949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fec72045e884'
down_revision = 'c3191b0280d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fav_caracteres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fav_caracteres')
    # ### end Alembic commands ###
