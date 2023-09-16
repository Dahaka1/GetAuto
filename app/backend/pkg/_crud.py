from typing import Type, TypeVar, Generic, Any, Optional, Sequence

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel

from . import SABase


ModelType = TypeVar("ModelType", bound=SABase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
CommonSchemaType = TypeVar("CommonSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType, CommonSchemaType]):
	def __init__(self, model: Type[ModelType], schema: Type[CommonSchemaType]):
		"""
		model: A SQLAlchemy model class
		schemas: A Pydantic model (schema) class
		"""
		self.model = model
		self.schema = schema

	async def get(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
		query = select(self.model).filter_by(id=id)
		result = await db.execute(query)
		return result.scalar()

	async def get_multi(
		self, db: AsyncSession, *, skip: int = 0, limit: int = 100
	) -> Sequence[ModelType]:
		query = select(self.model).offset(skip).limit(limit)
		result = await db.execute(query)
		return result.scalars().all()

	async def create(self, db: AsyncSession, *, obj_in: CreateSchemaType) -> CommonSchemaType:
		obj_in_data = jsonable_encoder(obj_in)
		db_obj = self.model(**obj_in_data)  # type: ignore
		db.add(db_obj)
		await db.commit()
		await db.refresh(db_obj)
		return db_obj

	@staticmethod
	async def update(
		db: AsyncSession,
		*,
		db_obj: ModelType,
		obj_in: UpdateSchemaType | dict[str, Any]
	) -> ModelType:
		obj_data = jsonable_encoder(db_obj)
		if isinstance(obj_in, dict):
			update_data = obj_in
		else:
			update_data = obj_in.model_dump(exclude_unset=True)
		for field in obj_data:
			if field in update_data:
				setattr(db_obj, field, update_data[field])
		await db.merge(db_obj)
		await db.commit()
		await db.refresh(db_obj)
		return db_obj

	async def remove(self, db: AsyncSession, *, id: int) -> ModelType:
		obj = self.get(db, id)
		await db.delete(obj)
		await db.commit()
		return obj
