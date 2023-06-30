from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.client.session.aiohttp import AiohttpSession

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = '6294776237:AAEQLWQUSq9dS9Zq-DS4nYiphKR12xHb7Ds'

session = AiohttpSession(proxy="http://10.26.145.5:8080/")
#bot = Bot('42:token', session=session)


# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN, session=session)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')
    # Если есть необходимость отправить в другой чат (пользователю)
    # await bot.send_message(message.chat.id, message.text)


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)