from vkbottle import BaseMiddleware, MiddlewareResponse
from vkbottle.bot import Message


class NoBotMiddleware(BaseMiddleware):
    """Проверяет, что тот, кто дал команду боту, сам не является ботом."""
    async def pre(self, message: Message):
        return MiddlewareResponse(message.from_id > 0)
