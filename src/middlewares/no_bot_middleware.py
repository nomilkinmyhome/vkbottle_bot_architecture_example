from vkbottle import BaseMiddleware
from vkbottle.bot import Message


class NoBotMiddleware(BaseMiddleware):
    """Проверяет, что тот, кто дал команду боту, сам не является ботом."""
    async def pre(self, message: Message):
        return message.from_id > 0
