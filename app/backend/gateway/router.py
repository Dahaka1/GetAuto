"""
Здесь в качестве маршрута нужно указывать только зарегистрированные УРЛ'ы.
"""
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from httpx import AsyncClient

from . import urls
from ._core import get_app_path, AppPath, app_request
from pkg import client as http_client
from .schemas import business
from urls import BusinessUrls

router = APIRouter(tags=["api"])


@router.post(urls.createUser.path, status_code=status.HTTP_201_CREATED, response_model=business.User)
async def create_user(
	app_path: Annotated[AppPath, Depends(get_app_path)],
	client: Annotated[AsyncClient, Depends(http_client)]
):
	response = await app_request(BusinessUrls.createUser, app_path, client)
	if response.status_code != 201:
		raise HTTPException(status_code=response.status_code, detail=response.json)
	return response


@router.get(urls.getUsers.path)
async def get_users(app_path: Annotated[AppPath, Depends(get_app_path)]):
	return {"answer": "test"}
