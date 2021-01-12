from sqlalchemy.sql import select

from src.models.db import session
from src.models.user import User


class UserRepository:
    def __init__(self, uid: int):
        self.uid = uid

    async def get_info_by_uid(self) -> str:
        query = select(User).where(User.c.uid == self.uid)
        user: User = await session.execute(query)
        info: str = self.prettify_info(user)
        return info

    @staticmethod
    def prettify_info(user: User) -> str:
        return f'ID: {user.uid}\n' \
               f'Имя: {user.first_name}\n' \
               f'Фамилия: {user.last_name}'
