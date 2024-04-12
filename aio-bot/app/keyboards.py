from aiogram.types import (ReplyKeyboardMarkup,  KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
# reply - интерфейс пользователя, при нажатии пишет текст в бота
# inline - клавиатура под постом

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'),
                                      KeyboardButton(text='/help')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')


catalog = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='✅  Одобрить', callback_data='aprove')],
                     [InlineKeyboardButton(
                         text='❌  Отклонить', callback_data='reject')],
                     # [InlineKeyboardButton(
                     #  text='📝  Поменять картинку', callback_data='rewrite')]
                     ])
