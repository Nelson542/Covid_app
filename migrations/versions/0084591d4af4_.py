"""empty message

Revision ID: 0084591d4af4
Revises: 31fa8a9fc3da
Create Date: 2022-06-30 15:24:26.228872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0084591d4af4'
down_revision = '31fa8a9fc3da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('Age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patients', 'Age')
    # ### end Alembic commands ###
