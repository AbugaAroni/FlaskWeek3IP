"""add a votes column to pitch class

Revision ID: 16f445a67a79
Revises: 8b87196cb604
Create Date: 2020-09-24 03:34:28.505532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16f445a67a79'
down_revision = '8b87196cb604'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch_votes', sa.Integer(), nullable=True))
    op.drop_column('pitches', 'votes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('votes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'pitch_votes')
    # ### end Alembic commands ###
