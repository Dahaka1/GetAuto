from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy import select

from ..schemas import (
	UserCreate, UserUpdate, EmployeeCreate,
	EmployeeUpdate, User as UserCommon, Employee as EmployeeCommon
)
from ..models import User, Employee
from pkg import CRUDBase
from pkg.logging import log


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate, UserCommon]):
	async def create(self, db, *, obj_in) -> UserCommon:
		user_db = await self.get_by_phone_number(db, obj_in.phone_number)
		if user_db:
			raise HTTPException(status_code=status.HTTP_409_CONFLICT,
								detail=f"Phone number {obj_in.phone_number} already exists")
		user_ = await super().create(db, obj_in=obj_in)
		log(f"User {user_.id} created", app="business")
		return user_

	async def get_by_phone_number(self, db, phone_number: str) -> Optional[UserCommon]:
		user_db_query = (
			select(self.model)
			.where(
				self.model.phone_number == phone_number
			)
		)
		result = (await db.execute(user_db_query)).scalar()
		return result


class CRUDEmployee(CRUDBase[Employee, EmployeeCreate, EmployeeUpdate, EmployeeCommon]):
	pass


user = CRUDUser(User, UserCommon)
employee = CRUDEmployee(Employee, EmployeeCommon)
