from telebot import TeleBot
from django.conf import settings


bot = TeleBot(token=settings.BOT_TOKEN)
