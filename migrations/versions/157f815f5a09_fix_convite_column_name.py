"""fix convite column name

Revision ID: 157f815f5a09
Revises: fd3541cfc5ca
Create Date: 2020-09-02 23:15:59.974401

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '157f815f5a09'
down_revision = 'fd3541cfc5ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('convidados', sa.Column('convite_uuid', sa.String(length=64), nullable=True))
    op.create_foreign_key(None, 'convidados', 'categorias', ['fk_categoria'], ['id'])
    op.create_foreign_key(None, 'convidados', 'noivos', ['fk_noivo'], ['id'])
    op.drop_column('convidados', 'convide_uuid')
    op.create_foreign_key(None, 'presentes', 'categorias', ['fk_categoria'], ['id'])
    op.create_foreign_key(None, 'presentes_comprados', 'presentes', ['fk_presente'], ['id'])
    op.create_foreign_key(None, 'referencia_presentes', 'presentes', ['fk_presente'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'referencia_presentes', type_='foreignkey')
    op.drop_constraint(None, 'presentes_comprados', type_='foreignkey')
    op.drop_constraint(None, 'presentes', type_='foreignkey')
    op.add_column('convidados', sa.Column('convide_uuid', mysql.VARCHAR(collation='utf8_unicode_ci', length=64), nullable=True))
    op.drop_constraint(None, 'convidados', type_='foreignkey')
    op.drop_constraint(None, 'convidados', type_='foreignkey')
    op.drop_column('convidados', 'convite_uuid')
    # ### end Alembic commands ###
