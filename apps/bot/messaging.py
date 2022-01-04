from telebot import types
from django.utils.translation import gettext_lazy as _
import telebot

from apps.bot import bot
from apps.bot import keyboards
from apps.bot.models import BotUser

def request_language(message):
    keyboard = keyboards.get_choose_language_keyboard()
    text = _('Choose language')
    bot.send_message(message.from_user.id, text=str(text), reply_markup=keyboard)


def request_full_name(message):
    keyboard = keyboards.remove_keyboard()
    text = _('Enter your full name')
    bot.send_message(message.from_user.id, text=str(text), reply_markup=keyboard)


def send_hello(message):
    user = BotUser.objects.filter(id=message.from_user.id).first()
    text = _('Hi! Nice to meet you again!')
    keyboard = keyboards.user_keyboard()
    bot.send_message(message.from_user.id, text=str(text),reply_markup=keyboard)

def request_number(message):
    keyboard = keyboards.share_contact_number()
    text = _('Please enter your phone number: ')
    bot.send_message(message.from_user.id, text=str(text), reply_markup=keyboard)

def congrat(message):
    user = BotUser.objects.filter(id=message.from_user.id).first()
    text1 = _("Dear")
    text2 = _("Thanks for registration")
    text = f"{text1} {user.full_name}, {text2}"
    keyboard = keyboards.user_keyboard()
    bot.send_message(message.from_user.id, text=str(text), reply_markup=keyboard)

def get_menu(message: types.Message):    
    
    text = str(_("What do you want to eat"))
    keyboard = keyboards.get_menu_keyboard()
    bot.send_message(message.from_user.id, text=str(text), reply_markup=keyboard)


def get_category_menu(message: types.Message,cat):    
    
    text = str(_("Choice food what do you want to eat"))
    keyboard = keyboards.get_product_menu_keyboard(cat)
    bot.send_message(message.from_user.id, text=str(text), reply_markup=keyboard)
    
def settings(message:types.Message):

    text = _("Please choice settings")
    keyboard = keyboards.setting_keyboard()
    bot.send_message(message.from_user.id, text=str(text), reply_markup=keyboard)

def change_name(message: types.Message):
    
    text = _("Input your new name")
    keyboard = keyboards.back()
    bot.send_message(message.from_user.id, text=str(text), reply_markup=keyboard)

def send_new_status(message: types.Message):

    user = BotUser.objects.filter(id=message.from_user.id).first()
    name = str(_("Full Name"))
    language = str (_("Language"))
    number = str (_("Phone Number"))

    text = f"Updated!\n {name}: {user.full_name}\n {language}: {user.locale}\n {number}: {user.phone_number}"
    
    keyboard = keyboards.setting_keyboard()
    bot.send_message(message.from_user.id, text=str(text), reply_markup=keyboard)

def back (message: types.Message):
    text = str(_("Return to Homepage"))
    keyboard = keyboards.user_keyboard()
    bot.send_message(chat_id =message.from_user.id ,text = text, reply_markup = keyboard)


def change_number(message):
    keyboard = keyboards.change_contact_number()
    text = _('Send your new number')
    bot.send_message(message.from_user.id, text=str(text), reply_markup=keyboard)

