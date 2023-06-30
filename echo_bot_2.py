from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.types import ContentType
from aiogram import F

from aiogram.client.session.aiohttp import AiohttpSession

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = ''

session = AiohttpSession(proxy="http://10.26.145.5:8080/")
#bot = Bot('42:token', session=session)


# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN, session=session)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')

# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)



# Aio метод send_copy
# @dp.message()
# async def send_echo(message: Message):
#    try:
#        await message.send_copy(chat_id=message.chat.id)
#    except TypeError:
#        await message.reply(text='Данный тип апдейтов не поддерживается '
#                                 'методом send_copy')




# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=['help']))

dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)

dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)