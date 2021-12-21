from django.utils.translation import gettext_lazy as _

from apps.bot import bot
from apps.bot import keyboards


def request_language(message):
    keyboard = keyboards.get_choose_language_keyboard()
    text = _('Choose language')
    bot.send_message(message.from_user.id, text=str(text), reply_markup=keyboard)


def request_full_name(message):
    keyboard = keyboards.remove_keyboard()
    text = _('Enter your full name')
    bot.send_message(message.from_user.id, text=str(text), reply_markup=keyboard)


def send_hello(message):
    text = _('Hi! Nice to meet you again!')
    bot.send_message(message.from_user.id, text=str(text))

def request_number(message):
    text = _('Please enter your phone number: ')
    bot.send_message(message.from_user.id, text=str(text))