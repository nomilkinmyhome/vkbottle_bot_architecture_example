from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from src.config import SQLALCHEMY_DATABASE_URI

engine = create_async_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base(bind=engine)
session = AsyncSession(bind=engine)
