from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
golos = dict()

# Кнопка-ссылка
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка_1', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка_2', url='https://google.com')
x = [
    InlineKeyboardButton(text='Ссылка_3', url='https://google.com'),
    InlineKeyboardButton(text='Ссылка_4', url='https://google.com'),
    InlineKeyboardButton(text='Ссылка_5', url='https://google.com')]
urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text='Ссылка_6', url='https://google.com'))

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Лайк', callback_data='like_1'),
                                             InlineKeyboardButton(text='Дизлайк', callback_data='like_-1'))

@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки:', reply_markup=urlkb)

@dp.message_handler(commands='test')
async def test_command(message: types.Message):
    await message.answer('Голосовать', reply_markup=inkb)

# @dp.callback_query_handler(text='www')
@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in golos:
        golos[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)
    # await callback.message.answer('Нажата инлайн кнопка')
    # await callback.answer('Нажата инлайн кнопка', show_alert=True)


executor.start_polling(dp, skip_updates=True)
