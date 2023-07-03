from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.filters import Text
from aiogram.types import Message
from aiogram.types import ContentType


from aiogram.client.session.aiohttp import AiohttpSession


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN: str = ''
session = AiohttpSession(proxy="http://10.26.145.5:8080/")



# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN, session=session)
dp: Dispatcher = Dispatcher()

admin_ids: list[int] = [123123123]

# Собственный фильтр, проверяющий юзера на админа
class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


# Этот фильтр будет проверять наличие неотрицательных чисел
# в сообщении от пользователя, и передавать в хэндлер их список
class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        # Разрезаем сообщение по пробелам, нормализуем каждую часть, удаляя
        # лишние знаки препинания и невидимые символы, проверяем на то, что
        # в таких словах только цифры, приводим к целым числам
        # и добавляем их в список
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        # Если в списке есть числа - возвращаем список по ключу 'numbers'
        if numbers:
            return {'numbers': numbers}
        return False








# Этот хэндлер будет срабатывать, если апдейт от админа
#@dp.message(IsAdmin(admin_ids))
#async def answer_if_admins_update(message: Message):
#    await message.answer(text='Вы админ')


# Этот хэндлер будет срабатывать, если апдейт не от админа
#@dp.message()
#async def answer_if_not_admins_update(message: Message):
#    await message.answer(text='Вы не админ')



# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа" и в нем есть числа
@dp.message(Text(startswith='найди числа', ignore_case=True),
            NumbersInMessage())
# Помимо объекта типа Message, принимаем в хэндлер список чисел из фильтра
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
            text=f'Нашел: {", ".join(str(num) for num in numbers)}')


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа", но в нем нет чисел
@dp.message(Text(startswith='найди числа', ignore_case=True))
async def process_if_not_numbers(message: Message):
    await message.answer(
            text='Не нашел что-то :(')







if __name__ == '__main__':
    dp.run_polling(bot)