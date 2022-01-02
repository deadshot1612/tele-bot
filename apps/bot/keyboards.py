from telebot import types
from django.utils.translation import gettext_lazy as _

from apps.bot.models import BotUser


def get_choose_language_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    for lang in BotUser.Locale.choices:
        keyboard.add(types.KeyboardButton(text=str(lang[1])))
    return keyboard

def share_contact_number():
    keyboard = types.ReplyKeyboardMarkup()
    text=_("Share your phone number")
    reg_button = types.KeyboardButton(text=str(text), request_contact=True)
    keyboard.add(reg_button)
    
    return keyboard
def admin_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    text=_("Add ad")
    button1 = types.KeyboardButton(text=str(text))
    button2 = types.KeyboardButton(text = str(_("Settings")))
    keyboard.add(button1,button2)

    return keyboard

def user_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton(text = str(_("Settings")))
    keyboard.add(button)

    return keyboard

def setting_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton(text= str(_("Change language")))
    button2 = types.KeyboardButton(text= str(_("Change Name")))
    button3 = types.KeyboardButton(text= str(_("Change Phone Number")))
    button4 = types.KeyboardButton(text= str(_("Back")))
    keyboard.add(button1,button2,button3, button4)

    return keyboard

def back():
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton(text= str(_("Back")))
    keyboard.add(button)

    return keyboard

def remove_keyboard():
    return types.ReplyKeyboardRemove()