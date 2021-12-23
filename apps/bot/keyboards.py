from telebot import types
from django.utils.translation import gettext_lazy as _

from apps.bot.models import BotUser


def get_choose_language_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    for lang in BotUser.Locale.choices:
        keyboard.add(types.KeyboardButton(text=str(lang[1])))
    return keyboard

def share_contact_number():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    text=_("Share your phone number")
    reg_button = types.KeyboardButton(text=str(text), request_contact=True)
    keyboard.add(reg_button)
    
    return keyboard

def remove_keyboard():
    return types.ReplyKeyboardRemove()