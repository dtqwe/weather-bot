from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main_kb = [
    [KeyboardButton(text='🇷🇺Россия'),
     KeyboardButton(text='🇰🇿Казахстан')],
     [KeyboardButton(text='🇺🇦Украина'),
     KeyboardButton(text='🇧🇾Беларусь')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb, resize_keyboard=True, input_field_placeholder='Выберите страну ниже:')

cityOfRu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Москва', callback_data='moscow')],
    [InlineKeyboardButton(text='Санкт-Петербург', callback_data='piter')],
    [InlineKeyboardButton(text='Казань', callback_data='kazan')],
    [InlineKeyboardButton(text='Омск', callback_data='omsk')],
    [InlineKeyboardButton(text='Назад', callback_data='backToMainfromRu')]
])

cityOfKz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Астана', callback_data='astana')],
    [InlineKeyboardButton(text='Алматы', callback_data='almaty')],
    [InlineKeyboardButton(text='Петропавловск', callback_data='petro')],
    [InlineKeyboardButton(text='Актобе', callback_data='aktobe')],
    [InlineKeyboardButton(text='Назад', callback_data='backToMainfromKz')]
])

cityOfUa = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Киев', callback_data='kiev')],
    [InlineKeyboardButton(text='Одесса', callback_data='odessa')],
    [InlineKeyboardButton(text='Львов', callback_data='lvov')],
    [InlineKeyboardButton(text='Днепр', callback_data='dnepr')],
    [InlineKeyboardButton(text='Назад', callback_data='backToMainfromUa')]
])

cityOfBy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Минск', callback_data='minsk')],
    [InlineKeyboardButton(text='Гомель', callback_data='gomel')],
    [InlineKeyboardButton(text='Витебск', callback_data='vitebsk')],
    [InlineKeyboardButton(text='Брест', callback_data='brest')],
    [InlineKeyboardButton(text='Назад', callback_data='backToMainfromUa')]
])