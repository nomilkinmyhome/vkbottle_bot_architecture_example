"""Blueprint для примера."""

from vkbottle.bot import Blueprint, Message

from src.repositories.user import UserRepository

bp = Blueprint(name='user')


@bp.on.message(text=['!инфа <uid:int>'])
async def info_handler(message: Message, uid: int):
    user_repository = UserRepository(uid=uid)
    user_info = await user_repository.get_info_by_uid()
    await message.answer(user_info)
