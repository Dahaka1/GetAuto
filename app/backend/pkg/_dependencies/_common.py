from sqlalchemy.ext.asyncio import AsyncSession

from .._database import async_session


async def session() -> AsyncSession:
	async with async_session() as s:
		yield s
