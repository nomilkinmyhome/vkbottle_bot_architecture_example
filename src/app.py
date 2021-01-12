import sys
import logging

from vkbottle.bot import Bot
from dotenv import load_dotenv

from src.blueprints import bps
from src.config import BOT_TOKEN
from src.middlewares.no_bot_middleware import NoBotMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

try:
    load_dotenv('.env')
except FileNotFoundError:
    logger.critical('No such .env file')
    sys.exit(1)


def init_bot():
    bot = Bot(token=BOT_TOKEN)
    setup_blueprints(bot)
    setup_middlewares(bot)
    return bot


def setup_blueprints(bot: Bot):
    for bp in bps:
        bp.load(bot)


def setup_middlewares(bot: Bot):
    bot.labeler.message_view.register_middleware(NoBotMiddleware())


bot = init_bot()
