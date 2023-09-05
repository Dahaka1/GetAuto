"""
Здесь в качестве маршрута нужно указывать только зарегистрированные УРЛ'ы.
"""
from typing import Annotated

from fastapi import APIRouter, status, Depends, Request

from . import urls
from ._core import get_app_path, AppPath


router = APIRouter(tags=["api"])


@router.post(urls.createUser.path)
async def create_user(
	app_path: Annotated[AppPath, Depends(get_app_path)]
):
	return {}


@router.get(urls.getUsers.path)
async def get_users(app_path: Annotated[AppPath, Depends(get_app_path)]):

	return {"answer": "test"}
