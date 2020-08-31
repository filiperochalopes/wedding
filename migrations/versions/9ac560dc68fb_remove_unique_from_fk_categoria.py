"""remove unique from fk categoria

Revision ID: 9ac560dc68fb
Revises: e8c62ccd186d
Create Date: 2020-08-30 15:25:31.720550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ac560dc68fb'
down_revision = 'e8c62ccd186d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('fk_categoria', table_name='convidados')
    op.drop_index('fk_noivo', table_name='convidados')
    op.create_foreign_key(None, 'convidados', 'noivos', ['fk_noivo'], ['id'])
    op.create_foreign_key(None, 'convidados', 'categorias', ['fk_categoria'], ['id'])
    op.drop_index('fk_categoria', table_name='presentes')
    op.create_foreign_key(None, 'presentes', 'categorias', ['fk_categoria'], ['id'])
    op.create_foreign_key(None, 'presentes_comprados', 'presentes', ['fk_presente'], ['id'])
    op.create_foreign_key(None, 'referencia_presentes', 'presentes', ['fk_presente'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'referencia_presentes', type_='foreignkey')
    op.drop_constraint(None, 'presentes_comprados', type_='foreignkey')
    op.drop_constraint(None, 'presentes', type_='foreignkey')
    op.create_index('fk_categoria', 'presentes', ['fk_categoria'], unique=True)
    op.drop_constraint(None, 'convidados', type_='foreignkey')
    op.drop_constraint(None, 'convidados', type_='foreignkey')
    op.create_index('fk_noivo', 'convidados', ['fk_noivo'], unique=True)
    op.create_index('fk_categoria', 'convidados', ['fk_categoria'], unique=True)
    # ### end Alembic commands ###
