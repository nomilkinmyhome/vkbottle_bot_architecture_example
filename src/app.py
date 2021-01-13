"""Сборка всего приложения."""
import logging

from vkbottle.bot import Bot

from src.blueprints import bps
from src.config import BOT_TOKEN
from src.middlewares.no_bot_middleware import NoBotMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def init_bot():
    """Фабрика для бота.

    Здесь также может быть инициализация других каких-нибудь сервисов
    (к примеру, redis) или прочие настройки, которые нужны проекту.
    """
    bot = Bot(token=BOT_TOKEN)
    setup_blueprints(bot)
    setup_middlewares(bot)
    return bot


def setup_blueprints(bot: Bot):
    """Инициализация blueprints."""
    for bp in bps:
        bp.load(bot)


def setup_middlewares(bot: Bot):
    """Инициализация middlewares."""
    bot.labeler.message_view.register_middleware(NoBotMiddleware())


bot = init_bot()
