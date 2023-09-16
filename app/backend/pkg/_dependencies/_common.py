from sqlalchemy.ext.asyncio import AsyncSession
from httpx import AsyncClient

from .._database import async_session


async def session() -> AsyncSession:
	async with async_session() as s:
		yield s


async def client() -> AsyncClient:
	async with AsyncClient() as c:
		yield c
