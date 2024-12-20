from typing import TypeVar, Generic
from sqlalchemy import update as sql_update, delete as sql_delete
from sqlalchemy.future import select
from sqlalchemy.orm import load_only
from app.config import db, commit_rollback

T = TypeVar('T')


class BaseRepo:
    model = Generic[T]

    @classmethod
    async def crear(cls, **kwargs):
        model = cls.model(**kwargs)
        db.add(model)
        await commit_rollback()
        return model

    @classmethod
    async def buscar_todo(cls, criterio_ordenamiento: str, columnas: list = None):
        if columnas is not None:
            columnas_consulta = [getattr(cls.model, col) for col in columnas]
            query = (select(cls.model).order_by(getattr(cls.model, criterio_ordenamiento)).
                     options(load_only(*columnas_consulta)))
        else:
            query = select(cls.model).order_by(getattr(cls.model, criterio_ordenamiento))
        return (await db.execute(query)).scalars()

    @classmethod
    async def buscar_por_id(cls, model_id: str, name_id: str):
        query = select(cls.model).where(getattr(cls.model, name_id) == model_id)
        return (await db.execute(query)).scalar_one_or_none()

    @classmethod
    async def actualizar_por_id(cls, model_id: str, name_id: str, **kwargs):
        query = sql_update(cls.model).where(getattr(cls.model, name_id) == model_id).values(**kwargs).execution_options(
            synchronize_session="fetch")
        await db.execute(query)
        await commit_rollback()

    @classmethod
    async def eliminar_por_id(cls, model_id: str, name_id: str):
        query = sql_delete(cls.model).where(getattr(cls.model, name_id) == model_id)
        await db.execute(query)
        await commit_rollback()
