from typing import Annotated

from fastapi import APIRouter, Body, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas import UserCreate, User
from pkg import session
from urls import BusinessUrls
from ..crud import user


router = APIRouter(tags=["users"])


@router.post(BusinessUrls.createUser, status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(
	user_: Annotated[UserCreate, Body(embed=True, alias="user")],
	db: Annotated[AsyncSession, Depends(session)]
):
	obj = await user.create(db, obj_in=user_)
	return obj
