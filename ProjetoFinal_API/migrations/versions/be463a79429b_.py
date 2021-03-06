"""empty message

Revision ID: be463a79429b
Revises: fbf2a234bb79
Create Date: 2022-04-25 19:29:32.331426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be463a79429b'
down_revision = 'fbf2a234bb79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contratos', 'termino_contrato')
    op.drop_column('contratos', 'inicio_contrato')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contratos', sa.Column('inicio_contrato', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('contratos', sa.Column('termino_contrato', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
