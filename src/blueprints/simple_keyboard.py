from vkbottle import Keyboard, KeyboardButtonColor, Callback
from vkbottle.bot import Blueprint, Message
from vkbottle_types import GroupTypes
from vkbottle_types.events import GroupEventType

from src.use_cases.random_number import get_random_number

bp = Blueprint()

# vbml_ignore_case включаем чтобы бот обрабатывал сообщение в любом регистре
# Например: если этот параметр будет False, то бот поймет только "!число", а если написать слово
# С заглавной буквы, то он уже не поймёт (!Число)
# Но если будет равен True, то бот поймет и "!ЧИСЛО", и "!ЧиСлО", и т.д.
bp.labeler.vbml_ignore_case = True

random_number_keyboard = (
    Keyboard(one_time=False, inline=True)
    .add(Callback("Еще число!", payload={"cmd": "more_numbers"}), color=KeyboardButtonColor.POSITIVE)
    .get_json()
)


@bp.on.message(text=["!число"])
async def random_number(message: Message):
    number = get_random_number()

    await message.answer(f"Выпало число — {number}!", keyboard=random_number_keyboard)


@bp.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def message_event(event: GroupTypes.MessageEvent):
    if event.object.payload["cmd"] == "more_numbers":
        number = get_random_number()

        await bp.api.messages.edit(
            peer_id=event.object.peer_id,
            conversation_message_id=event.object.conversation_message_id,
            message=f"Выпало число — {number}!",
            keyboard=random_number_keyboard
        )
