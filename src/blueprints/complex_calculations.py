"""Blueprint для примера."""

from vkbottle.bot import Blueprint, Message

from src.use_cases.complex_calculations import calculate_something

bp = Blueprint(name='complex_calculations')


@bp.on.message(text=['!посчитай'])
async def calculation_handler(message: Message):
    complex_calculation_result = calculate_something()
    await message.answer(complex_calculation_result)
