from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker

import config


def create_engine(url: URL | str) -> AsyncEngine:
    engine = create_async_engine(url=url, echo=True, pool_pre_ping=True)
    return engine


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False
    )