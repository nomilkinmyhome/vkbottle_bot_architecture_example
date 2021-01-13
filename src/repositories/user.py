"""Реализация паттерна Repository для сущности User."""
from typing import Optional

from sqlalchemy.sql import select

from src.models.db import engine
from src.models.user import User


class UserRepository:
    def __init__(self, uid: int):
        self.uid = uid

    async def get_info_by_uid(self) -> str:
        """Получить информацию о пользователе из БД и
        вернуть ее в красивом виде."""
        async with engine.connect() as conn:
            query = select(User).where(User.uid == self.uid)
            user: Optional[User] = (await conn.execute(query)).fetchone()
            return self.prettify_info(user)

    @staticmethod
    def prettify_info(user: Optional[User]) -> str:
        """Сформировать строку с информацией о юзере."""
        if user:
            return f'ID: {user.uid}\n' \
                   f'Имя: {user.first_name}\n' \
                   f'Фамилия: {user.last_name}'
        return 'Такого пользователя нет в базе данных.'
