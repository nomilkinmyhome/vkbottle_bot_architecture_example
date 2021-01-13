"""Конфиг проекта."""
from envparse import env

env.read_envfile('.env')

BOT_TOKEN = env.str('BOT_TOKEN')

POSTGRES_HOST = env.str('POSTGRES_HOST', default='localhost')
POSTGRES_PORT = env.str('POSTGRES_PORT', default=5432)
POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD')
POSTGRES_USER = env.str('POSTGRES_USER')
POSTGRES_DB = env.str('POSTGRES_DB')
SQLALCHEMY_DATABASE_URI = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'  # noqa
SQLALCHEMY_TRACK_MODIFICATIONS = False
