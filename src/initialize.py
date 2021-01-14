"""Подготовка БД."""
from src.models.db import Base, engine


async def setup_db():
    """Очистить базу данных и создать таблицы по описанным моделям."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
