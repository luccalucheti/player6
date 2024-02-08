"""Initial migration.

Revision ID: 2a04aba4e1fd
Revises: 
Create Date: 2024-01-24 16:55:45.449085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a04aba4e1fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('register',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('player1', sa.String(length=25), nullable=False),
    sa.Column('player2', sa.String(length=25), nullable=False),
    sa.Column('player3', sa.String(length=25), nullable=False),
    sa.Column('player4', sa.String(length=25), nullable=False),
    sa.Column('player5', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('player1'),
    sa.UniqueConstraint('player2'),
    sa.UniqueConstraint('player3'),
    sa.UniqueConstraint('player4'),
    sa.UniqueConstraint('player5'),
    sa.UniqueConstraint('team')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('register')
    # ### end Alembic commands ###