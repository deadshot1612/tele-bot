from telebot import types
from django.utils.translation import gettext_lazy as _

from apps.bot.models import BotUser
from apps.product.views import all_categories, get_product_from_category
def get_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button = types.KeyboardButton(text= str(_("Back")))
    categories = all_categories()
    for cat in categories:
        keyboard.add(types.KeyboardButton(text=str(cat.name)))
    keyboard.add(button)
    return keyboard


def get_product_menu_keyboard(cat):
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton(text= str(_("Back")))
    products = get_product_from_category(cat)
    for p in products:
        keyboard.add(types.KeyboardButton(text=str(p.name)))
    keyboard.add(button)
    return keyboard

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


def user_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton(text = str(_("Settings")))
    button2 = types.KeyboardButton(text = str(_("Menu")))
    keyboard.add(button1,button2)

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

def change_contact_number():
    keyboard = types.ReplyKeyboardMarkup()
    text=_("Share your phone number")
    reg_button = types.KeyboardButton(text=str(text), request_contact=True)
    text=_("Back")
    button = types.KeyboardButton(text=str(text))
    keyboard.add(reg_button, button)
    
    return keyboard
def remove_keyboard():
    return types.ReplyKeyboardRemove()