"""Initial real tables

Revision ID: 255509338bcf
Revises: e856cf5b536e
Create Date: 2020-06-21 14:31:55.509879

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '255509338bcf'
down_revision = 'e856cf5b536e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doacoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('valor', sa.Float(), nullable=True),
    sa.Column('mensagem', sa.Text(), nullable=True),
    sa.Column('id_transacao', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mensagens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('mensagem', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('noivos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('senha', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('presentes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=128), nullable=True),
    sa.Column('imagem', sa.String(length=128), nullable=True),
    sa.Column('preco', sa.Float(precision=10, asdecimal=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('convidados',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=True),
    sa.Column('numero_convidados', sa.Integer(), nullable=True),
    sa.Column('confirmou_presenca', sa.DateTime(), nullable=True),
    sa.Column('fk_noivo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fk_noivo'], ['noivos.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('fk_noivo'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('presentes_comprados',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('fk_presente', sa.Integer(), nullable=True),
    sa.Column('mensagem', sa.Text(), nullable=True),
    sa.Column('id_transacao', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['fk_presente'], ['presentes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('referencia_presentes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link_referencia', sa.Text(), nullable=True),
    sa.Column('fk_presente', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fk_presente'], ['presentes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('follow')
    op.drop_index('email', table_name='users')
    op.drop_index('username', table_name='users')
    op.drop_table('users')
    op.drop_table('gifts')
    op.drop_table('posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('content', mysql.TEXT(collation='utf8_unicode_ci'), nullable=True),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('gifts',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(collation='utf8_unicode_ci', length=64), nullable=True),
    sa.Column('price', mysql.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(collation='utf8_unicode_ci', length=64), nullable=True),
    sa.Column('password', mysql.VARCHAR(collation='utf8_unicode_ci', length=64), nullable=True),
    sa.Column('name', mysql.VARCHAR(collation='utf8_unicode_ci', length=64), nullable=True),
    sa.Column('email', mysql.VARCHAR(collation='utf8_unicode_ci', length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_index('username', 'users', ['username'], unique=True)
    op.create_index('email', 'users', ['email'], unique=True)
    op.create_table('follow',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('follow_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.drop_table('referencia_presentes')
    op.drop_table('presentes_comprados')
    op.drop_table('convidados')
    op.drop_table('presentes')
    op.drop_table('noivos')
    op.drop_table('mensagens')
    op.drop_table('doacoes')
    # ### end Alembic commands ###
