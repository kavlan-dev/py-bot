import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from py_bot.config import load_config
from py_bot.depends import get_dog_service

dp = Dispatcher()
dog_service = get_dog_service()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    msg = "Привет!"
    if message.from_user and message.from_user.full_name:
        msg = f"Привет, {message.from_user.full_name}!"
    await message.answer(msg)


@dp.message(Command("dog"))
async def random_dog_handler(message: Message) -> None:
    url = dog_service.get_random_dog()
    if url:
        await message.answer_photo(url)
        return
    await message.answer("Произошла ошибка")


@dp.message()
async def echo_handler(message: Message) -> None:
    if message.text:
        await message.reply(message.text)
        return
    await message.answer("Хорошая попытка!")


async def main() -> None:
    config = load_config()
    if not config.get_token():
        logging.error("TOKEN не указан")
        return

    bot = Bot(
        token=config.get_token(),
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
