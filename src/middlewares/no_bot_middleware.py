from vkbottle import BaseMiddleware


class NoBotMiddleware(BaseMiddleware):
    """Проверяет, что тот, кто дал команду боту, сам не является ботом."""
    async def pre(self):
        if self.event.from_id < 0:
            self.stop("Отправитель является ботом")
