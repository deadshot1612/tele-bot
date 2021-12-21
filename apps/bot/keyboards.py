from telebot import types

from apps.bot.models import BotUser


def get_choose_language_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    for lang in BotUser.Locale.choices:
        keyboard.add(types.KeyboardButton(text=str(lang[1])))
    return keyboard


def remove_keyboard():
    return types.ReplyKeyboardRemove()