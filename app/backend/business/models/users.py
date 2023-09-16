import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func, Enum, Column, ForeignKey, BIGINT
from sqlalchemy.ext.hybrid import hybrid_property

from pkg import SABase
import enums


class User(SABase):
	__tablename__ = "users"

	id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
	_phone_number: Mapped[str] = mapped_column('phone_number', unique=True, nullable=False)
	first_name: Mapped[str] = mapped_column(nullable=False)
	registered_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
	is_disabled: Mapped[bool] = mapped_column(default=False)
	came_from = Column(Enum(enums.CameFromEnum))

	@hybrid_property
	def phone_number(self):
		return str(self._phone_number).lstrip("tel:")

	@phone_number.setter
	def phone_number(self, phone_number):
		self._phone_number = phone_number


class Employee(SABase):
	__tablename__ = "employers"

	id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
	user_id = mapped_column(ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"))
	last_name: Mapped[str] = mapped_column(nullable=False)
	role = Column(Enum(enums.EmployeeRoleEnum), nullable=False)
	telegram_chat_id: Mapped[int] = mapped_column(BIGINT, nullable=True, unique=True)
