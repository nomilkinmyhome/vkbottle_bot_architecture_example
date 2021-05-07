"""Сборка всего приложения."""
import logging

from vkbottle.bot import Bot
from vkbottle.tools.dev_tools.loop_wrapper import LoopWrapper

from src.blueprints import bps
from src.config import BOT_TOKEN
from src.initialize import setup_db
from src.middlewares.no_bot_middleware import NoBotMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def init_bot():
    """Фабрика для бота.

    Здесь также может быть инициализация других каких-нибудь сервисов
    (к примеру, redis) или прочие настройки, которые нужны проекту.
    """
    bot_ = Bot(token=BOT_TOKEN,
               loop_wrapper=LoopWrapper(on_startup=[setup_db()]))
    setup_blueprints(bot_)
    setup_middlewares(bot_)
    return bot_


def setup_blueprints(bot_: Bot):
    """Инициализация blueprints."""
    for bp in bps:
        bp.load(bot_)


def setup_middlewares(bot_: Bot):
    """Инициализация middlewares."""
    bot_.labeler.message_view.register_middleware(NoBotMiddleware)


bot = init_bot()
