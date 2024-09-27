from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import table, Column, String
from typing import Optional, List


from app.model.mixins import TimeMixin
from app.model.actividad_entrenador import ActividadEntrenador


class Actividad(SQLModel, TimeMixin, table=True):
    __tablename__ = "actividad"

    ID_actividad: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    nombre: str = Field(sa_column=Column("nombre", String, unique=True))
    descripcion: str

    citas_actividad: List["Cita"] = Relationship(back_populates="actividad")

    entrenador_actividad: List["Entrenador"] = Relationship(back_populates="actividad", link_model=ActividadEntrenador)