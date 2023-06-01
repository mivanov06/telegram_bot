from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CALL_US_BUTTON = ('Позвонить нам', 'call_us')

START_KEYBOARD = [
    ('Да, хочу!', 'Да, хочу!'),
]


def get_inline_keyboard(query, buttons_in_row=2, back_menu=False) -> InlineKeyboardMarkup:
    buttons_row = []
    inline_keyboard = []
    if back_menu:
        buttons_row.append(InlineKeyboardButton(text='<= Назад', callback_data='menu8'))
        inline_keyboard.append(buttons_row)
        buttons_row = []
    for element in query:
        text, data = element
        buttons_row.append(InlineKeyboardButton(text=text, callback_data=data))
        if len(buttons_row) == buttons_in_row:
            inline_keyboard.append(buttons_row)
            buttons_row = []
    if buttons_row:
        inline_keyboard.append(buttons_row)
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)