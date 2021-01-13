"""Подготовка БД."""
import asyncio

from src.models.db import Base, engine


async def setup_db():
    """Очистить базу данных и создать таблицы по описанным моделям."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(setup_db())
