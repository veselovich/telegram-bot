from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text='/create'), KeyboardButton(text='/search'))
    return kb

def get_cancel_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text='/cancel'))
    return kb

def get_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ikb.add(InlineKeyboardButton(text='Next',
                                 callback_data='next'))
    return ikb