import datetime
from typing import Optional

from pydantic import BaseModel, Field
from pydantic_extra_types.phone_numbers import PhoneNumber

from enums import CameFromEnum, EmployeeRoleEnum


class UserBase(BaseModel):
	phone_number: PhoneNumber
	first_name: str
	is_disabled: bool
	came_from: Optional[CameFromEnum]


class UserCreate(UserBase):
	first_name: str = Field(max_length=20)
	is_disabled: Optional[bool] = Field(exclude=True, default=False)
	came_from: Optional[CameFromEnum] = None


class User(UserBase):
	id: int
	registered_at: datetime.datetime

	class Config:
		from_attributes = True


class UserUpdate(BaseModel):
	phone_number: Optional[PhoneNumber]
	first_name: Optional[str]
	is_disabled: Optional[bool]


class EmployeeCreate(UserCreate):
	user_id: int
	last_name: str = Field(max_length=30)
	role: EmployeeRoleEnum
	telegram_chat_id: int


class Employee(EmployeeCreate):
	id: int

	class Config:
		from_attributes = True


class EmployeeUpdate(Employee):
	last_name: Optional[str]
	role: Optional[EmployeeRoleEnum]
	telegram_chat_id: Optional[int]
