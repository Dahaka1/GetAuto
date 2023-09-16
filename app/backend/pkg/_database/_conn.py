from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

import config


DATABASE_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(*config.DB_PARAMS)


engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, autoflush=False)
