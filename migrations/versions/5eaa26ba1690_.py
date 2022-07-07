"""empty message

Revision ID: 5eaa26ba1690
Revises: 539c9fc36e04
Create Date: 2022-07-01 20:33:28.241061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5eaa26ba1690'
down_revision = '539c9fc36e04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('patients', 'TestResult',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
    op.alter_column('patients', 'Status',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('patients', 'Status',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
    op.alter_column('patients', 'TestResult',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
    # ### end Alembic commands ###
