from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import table, Enum, Column, String
from typing import Optional, List
from datetime import date

from app.model.mixins import TimeMixin
from app.model.Proveedores import Proveedores


class Sexo(str, Enum):
    MASCULINO = "MASCULINO"
    FEMENINO = "FEMENINO"


class Administradores(SQLModel, TimeMixin, table=True):
    __tablename__ = "administradores"

    ID_admin: Optional[str] = Field(default=None, primary_key=True, nullable=False)
    nombre: str
    segundo_nombre: Optional[str] = None
    apellido: str
    segundo_apellido: Optional[str] = None
    fecha_nacimiento: date
    sexo: Sexo
    correo: str = Field(sa_column=Column("correo", String, unique=True))
    telefono: str

    proveedores: List["Proveedores"] = Relationship(back_populates="administradores",
                                                    sa_relationship_kwargs={'cascade': "all, delete-orphan"})
