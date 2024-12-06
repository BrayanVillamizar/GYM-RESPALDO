"""Edited tables

Revision ID: bc577fb26921
Revises: 
Create Date: 2024-11-18 18:31:44.412602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel 

# revision identifiers, used by Alembic.
revision: str = '5d3e3040618a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrador',
    sa.Column('creado_en', sa.DateTime(), nullable=False),
    sa.Column('modificado_en', sa.DateTime(), nullable=False),
    sa.Column('ID_admin', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('sexo', sa.String(), nullable=True),
    sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('segundo_nombre', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('apellido', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('segundo_apellido', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=False),
    sa.Column('correo', sa.String(), nullable=True),
    sa.Column('direccion', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('telefono', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('rango', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('ID_admin'),
    sa.UniqueConstraint('correo')
    )
    op.create_table('cliente',
    sa.Column('creado_en', sa.DateTime(), nullable=False),
    sa.Column('modificado_en', sa.DateTime(), nullable=False),
    sa.Column('ID_cliente', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('sexo', sa.String(), nullable=True),
    sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('segundo_nombre', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('apellido', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('segundo_apellido', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=False),
    sa.Column('correo', sa.String(), nullable=True),
    sa.Column('telefono', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('direccion', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.Column('peso', sa.Float(), nullable=False),
    sa.Column('altura', sa.Float(), nullable=False),
    sa.Column('rango', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ID_titular', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['ID_titular'], ['cliente.ID_cliente'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('ID_cliente'),
    sa.UniqueConstraint('correo')
    )
    op.create_table('entrenador',
    sa.Column('creado_en', sa.DateTime(), nullable=False),
    sa.Column('modificado_en', sa.DateTime(), nullable=False),
    sa.Column('ID_entrenador', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('sexo', sa.String(), nullable=True),
    sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('segundo_nombre', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('apellido', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('segundo_apellido', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=False),
    sa.Column('correo', sa.String(), nullable=True),
    sa.Column('telefono', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('direccion', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('especialidad', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.Column('rango', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('ID_entrenador'),
    sa.UniqueConstraint('correo')
    )
    op.create_table('actividad',
    sa.Column('creado_en', sa.DateTime(), nullable=False),
    sa.Column('modificado_en', sa.DateTime(), nullable=False),
    sa.Column('ID_actividad', sa.Integer(), nullable=False),
    sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('precio', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('hora', sa.Time(), nullable=False),
    sa.Column('duracion_minutos', sa.Integer(), nullable=False),
    sa.Column('lugar', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ID_entrenador', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['ID_entrenador'], ['entrenador.ID_entrenador'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('ID_actividad')
    )
    op.create_table('entrenamiento',
    sa.Column('creado_en', sa.DateTime(), nullable=False),
    sa.Column('modificado_en', sa.DateTime(), nullable=False),
    sa.Column('ID_entrenamiento', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tipo', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ID_entrenador', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('ID_cliente', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['ID_cliente'], ['cliente.ID_cliente'], ),
    sa.ForeignKeyConstraint(['ID_entrenador'], ['entrenador.ID_entrenador'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('ID_entrenamiento')
    )
    op.create_table('membresia',
    sa.Column('creado_en', sa.DateTime(), nullable=False),
    sa.Column('modificado_en', sa.DateTime(), nullable=False),
    sa.Column('ID_membresia', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('descuento', sa.Float(), nullable=False),
    sa.Column('max_miembros', sa.Integer(), nullable=False),
    sa.Column('precio', sa.Integer(), nullable=False),
    sa.Column('duracion_meses', sa.Integer(), nullable=False),
    sa.Column('ID_admin_creador', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['ID_admin_creador'], ['administrador.ID_admin'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('ID_membresia')
    )
    op.create_table('proveedor',
    sa.Column('creado_en', sa.DateTime(), nullable=False),
    sa.Column('modificado_en', sa.DateTime(), nullable=False),
    sa.Column('ID_proveedor', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('telefono', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('direccion', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('correo', sa.String(), nullable=True),
    sa.Column('producto', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ID_admin_creador', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['ID_admin_creador'], ['administrador.ID_admin'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('ID_proveedor'),
    sa.UniqueConstraint('correo')
    )
    op.create_table('cita',
    sa.Column('creado_en', sa.DateTime(), nullable=False),
    sa.Column('modificado_en', sa.DateTime(), nullable=False),
    sa.Column('ID_cita', sa.Integer(), nullable=False),
    sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('hora', sa.Time(), nullable=False),
    sa.Column('duracion_minutos', sa.Integer(), nullable=False),
    sa.Column('lugar', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ID_cliente', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('ID_actividad', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ID_actividad'], ['actividad.ID_actividad'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ID_cliente'], ['cliente.ID_cliente'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('ID_cita')
    )
    op.create_table('compra_membresia',
    sa.Column('creado_en', sa.DateTime(), nullable=False),
    sa.Column('modificado_en', sa.DateTime(), nullable=False),
    sa.Column('ID_comprador', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ID_membresia', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('metodo_pago', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tipo_compra', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['ID_comprador'], ['cliente.ID_cliente'], ),
    sa.ForeignKeyConstraint(['ID_membresia'], ['membresia.ID_membresia'], ),
    sa.PrimaryKeyConstraint('ID_comprador', 'ID_membresia')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('compra_membresia')
    op.drop_table('cita')
    op.drop_table('proveedor')
    op.drop_table('membresia')
    op.drop_table('entrenamiento')
    op.drop_table('actividad')
    op.drop_table('entrenador')
    op.drop_table('cliente')
    op.drop_table('administrador')
    # ### end Alembic commands ###