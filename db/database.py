from typing import AsyncGenerator
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from decouple import config


driver = "postgresql+asyncpg"

database_name = config('DATABASE_NAME')
host = config('DATABASE_HOST')
port = config('DATABASE_PORT')
user = config('DATABASE_USER')
password = config('DATABASE_PASSWORD')

DATABASE_URL = URL.create(
    database=database_name,
    username=user,
    password=password,
    host=host,
    port=port,
    drivername=driver
)


engine = create_async_engine(
    DATABASE_URL, echo=False
)

async_session_maker = async_sessionmaker(
    engine, expire_on_commit=True
)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
