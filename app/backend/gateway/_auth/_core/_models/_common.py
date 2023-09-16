import datetime

from sqlalchemy import Enum, Column, DateTime, ForeignKey, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from pkg import SABase, session
from ...enums import AuthTypeEnum
from .._exceptions import NotAuthenticatedError


class AuthenticationBase(SABase):
	"""
	subject - ТГ-чат админа или номер телефона пользователя
	"""
	__tablename__ = "auth"

	subject: Mapped[str] = mapped_column(nullable=False, primary_key=True, index=True)
	user_id = mapped_column(ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"))
	type = Column(Enum(AuthTypeEnum), nullable=False)
	refresh: Mapped[str] = mapped_column(nullable=False)
	expires_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False)
	last_auth_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))


class Authentication:
	_model = AuthenticationBase

	def __init__(self, subject: str, type_: AuthTypeEnum):
		self.__subject = subject
		self.exists = False
		self.user_id = None
		self.refresh = None
		self.type = type_
		self.expires_at = None
		self.accessed_subjects = []

	def __getattr__(self, item):
		try:
			attr = self.__dict__[item]
		except KeyError:
			raise AttributeError(item)
		if attr is None:
			raise AttributeError("Attribute wasn't defined. Use '__aenter__' to define")
		return attr

	async def __aenter__(self):
		async with session() as db:
			query = select(self._model).where((self._model.subject == self.__subject) &
											 (self._model.type == self.type))
			result = await db.execute(query)
			obj_db = result.scalar()
			if obj_db:
				self.exists = True
				self.user_id = obj_db.user_id
				self.refresh = obj_db.refresh
				self.expires_at = obj_db.expires_at
				if self.expires_at < datetime.datetime.now():
					raise NotAuthenticatedError()
				await self._update_last_auth(db)
		return self

	async def __aexit__(self, exc_type, exc_val, exc_tb):
		pass

	async def _update_last_auth(self, db: AsyncSession) -> None:
		query = update(self._model).where(self._model.subject == self.__subject).values(
			last_auth_at=datetime.datetime.now()
		)
		await db.execute(query)
		await db.commit()
