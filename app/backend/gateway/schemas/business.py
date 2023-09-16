from typing import Optional
import datetime

from pydantic import BaseModel, Field
from pydantic_extra_types.phone_numbers import PhoneNumber

from enums import CameFromEnum


class UserBase(BaseModel):
	phone_number: PhoneNumber
	first_name: str
	is_disabled: bool
	came_from: Optional[CameFromEnum]


class UserCreate(UserBase):
	first_name: str = Field(max_length=20)
	is_disabled: Optional[bool] = False


class User(UserBase):
	id: int
	registered_at: datetime.datetime
