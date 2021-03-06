"""fix db errors and add user profile

Revision ID: 1a2b2fb714d1
Revises: 3cd1d8901998
Create Date: 2020-09-23 21:42:23.746284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a2b2fb714d1'
down_revision = '3cd1d8901998'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch_title', sa.String(), nullable=True),
    sa.Column('pitch_category', sa.String(), nullable=True),
    sa.Column('pitch_description', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitches')
    # ### end Alembic commands ###
